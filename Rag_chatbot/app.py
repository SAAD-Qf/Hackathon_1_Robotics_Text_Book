import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
HF_EMBEDDING_MODEL = os.getenv("HF_EMBEDDING_MODEL")
HF_GENERATION_MODEL = os.getenv("HF_GENERATION_MODEL")
BOOK_CONTENT_PATH = os.getenv("BOOK_CONTENT_PATH")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH")

logger.info(f"HF_EMBEDDING_MODEL: {HF_EMBEDDING_MODEL}")
logger.info(f"HF_GENERATION_MODEL: {HF_GENERATION_MODEL}")
logger.info(f"BOOK_CONTENT_PATH: {BOOK_CONTENT_PATH}")
logger.info(f"FAISS_INDEX_PATH: {FAISS_INDEX_PATH}")


# --- Global variables for RAG components ---
embedding_model = None
generation_tokenizer = None
generation_model = None
faiss_index = None
text_chunks = []


# --- RAG Core Functions ---
async def load_rag_models():
    """Loads the embedding and generation models."""
    global embedding_model, generation_tokenizer, generation_model
    logger.info("Loading RAG models...")
    try:
        embedding_model = SentenceTransformer(HF_EMBEDDING_MODEL)
        generation_tokenizer = AutoTokenizer.from_pretrained(HF_GENERATION_MODEL)
        # Corrected model class for T5-based models
        generation_model = AutoModelForSeq2SeqLM.from_pretrained(HF_GENERATION_MODEL)
        logger.info("RAG models loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading RAG models: {e}")
        raise

async def load_and_process_book_content():
    """
    Loads book content, splits it into chunks, generates embeddings,
    and creates/loads a FAISS index.
    """
    global faiss_index, text_chunks
    logger.info("Loading and processing book content...")
    try:
        if not BOOK_CONTENT_PATH or not os.path.exists(BOOK_CONTENT_PATH):
            logger.error(f"Book content path not found: {BOOK_CONTENT_PATH}")
            raise FileNotFoundError(f"BOOK_CONTENT_PATH not found: {BOOK_CONTENT_PATH}")

        with open(BOOK_CONTENT_PATH, "r", encoding="utf-8") as f:
            book_text = f.read()

        # Simple text splitting by double newline
        raw_chunks = book_text.split("\n\n")
        text_chunks = [chunk.strip() for chunk in raw_chunks if chunk.strip()]

        if os.path.exists(FAISS_INDEX_PATH):
            logger.info(f"Loading FAISS index from {FAISS_INDEX_PATH}")
            faiss_index = faiss.read_index(FAISS_INDEX_PATH)
        else:
            logger.info("Creating new FAISS index...")
            if not embedding_model:
                await load_rag_models()

            chunk_embeddings = embedding_model.encode(text_chunks, convert_to_tensor=True).cpu().numpy()
            dimension = chunk_embeddings.shape[1]
            faiss_index = faiss.IndexFlatL2(dimension)
            faiss_index.add(chunk_embeddings)
            faiss.write_index(faiss_index, FAISS_INDEX_PATH)
            logger.info(f"FAISS index created and saved to {FAISS_INDEX_PATH}")

        logger.info("Book content processed and FAISS index ready.")
    except Exception as e:
        logger.error(f"Error processing book content or FAISS index: {e}")
        raise

# --- FastAPI Application ---
app = FastAPI(
    title="RAG Chatbot API",
    description="A simple Retrieval-Augmented Generation chatbot API.",
    version="0.1.0",
)

@app.on_event("startup")
async def startup_event():
    """Load RAG models and process book content during application startup."""
    await load_rag_models()
    await load_and_process_book_content()

@app.get("/")
async def read_root():
    """Root endpoint for the RAG Chatbot API."""
    return {"message": "Welcome to the RAG Chatbot API!"}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_rag(request: ChatRequest):
    """
    Chat endpoint for the RAG Chatbot API.
    Receives a user message, retrieves relevant context, and generates a response.
    """
    if not all([embedding_model, faiss_index, generation_tokenizer, generation_model]):
        logger.error("RAG models or FAISS index not loaded.")
        return {"response": "Chatbot is not ready. Please try again later."}

    user_query = request.message
    logger.info(f"Received query: {user_query}")

    try:
        # Retrieve context
        query_embedding = embedding_model.encode([user_query], convert_to_tensor=True).cpu().numpy()
        D, I = faiss_index.search(query_embedding, k=3)
        
        retrieved_chunks = [text_chunks[idx] for idx in I[0] if idx < len(text_chunks)]
        context = "\n".join(retrieved_chunks)
        logger.info(f"Retrieved context: {context[:200]}...")

        # Generate response
        prompt = f"Context: {context}\nQuestion: {user_query}\nAnswer:"
        
        generator = pipeline("text2text-generation", model=generation_model, tokenizer=generation_tokenizer)
        response_text = generator(prompt, max_new_tokens=100, num_return_sequences=1)[0]["generated_text"]

        logger.info(f"Generated response: {response_text}")
        return {"response": response_text}

    except Exception as e:
        logger.error(f"Error during RAG chat: {e}")
        return {"response": "An error occurred while processing your request."}
