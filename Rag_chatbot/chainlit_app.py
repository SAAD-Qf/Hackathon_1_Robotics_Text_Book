import chainlit as cl
import requests

FASTAPI_URL = "http://localhost:8000" # Assuming FastAPI is running on this URL

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to the RAG Chatbot! Ask me anything about the book content.",
    ).send()

@cl.on_message
async def main(message: cl.Message):
    response = requests.post(
        f"{FASTAPI_URL}/chat",
        json={"message": message.content}
    )

    if response.status_code == 200:
        bot_message = response.json().get("response", "An error occurred while getting response from the RAG backend.")
    else:
        bot_message = f"Error from RAG backend: {response.status_code} - {response.text}"
    
    await cl.Message(
        content=bot_message,
    ).send()

