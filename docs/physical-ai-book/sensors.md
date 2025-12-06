---
title: Sensors in Robotics
slug: /physical-ai-book/sensors
sidebar_label: Sensors
sidebar_position: 3
---

# Understanding Sensors in Robotics

Sensors are the **eyes, ears, and skin** of robots. They allow humanoid robots to perceive the environment, understand their own state, and make decisions based on real-world data.

## Types of Sensors

1. **Vision Sensors**  
   - Cameras, RGB-D cameras, LIDAR  
   - Capture images, depth, and 3D structure for navigation and object recognition  

2. **Inertial Sensors (IMU)**  
   - Accelerometers and gyroscopes  
   - Measure orientation, acceleration, and angular velocity for balance and motion control  

3. **Force and Tactile Sensors**  
   - Measure pressure, touch, or force applied on limbs  
   - Crucial for grasping objects safely  

4. **Proximity Sensors**  
   - Ultrasonic, infrared  
   - Detect nearby objects and prevent collisions  

## Why Sensors Matter

- Enable real-time decision-making  
- Allow robots to interact safely with humans and objects  
- Provide feedback for precise movement and balance  
- Serve as the foundation for AI perception modules

## Learning Outcomes

By the end of this chapter, you will be able to:
- Identify major sensors used in humanoid robotics  
- Explain how sensors collect and process data  
- Understand sensor calibration and integration  
- Appreciate the role of sensors in perception, planning, and control

## Practical Lab Exercise

**Objective:** Collect and process data from a sensor.

**Steps:**
1. Connect a LIDAR or ultrasonic sensor to a microcontroller or Jetson board.  
2. Use Python to read distance measurements.  
3. Plot the data in real-time using matplotlib.  
4. Add a threshold to trigger an alert if an object is too close.  

**Expected Output:**  
- Real-time sensor readings are visualized on a graph.  
- Robot can detect nearby obstacles and react accordingly.

## Troubleshooting

1. **No sensor data:** Check connections and power supply.  
2. **Incorrect readings:** Calibrate sensor using manufacturer instructions.  
3. **Data lag:** Optimize Python code and reduce loop delay.

## Quiz (5 MCQs)

1. Which sensor helps robots detect objects around them?  
   - A) IMU  
   - B) LIDAR ✅  
   - C) Servo motor  
   - D) Microphone  

2. What does an IMU measure?  
   - A) Distance  
   - B) Orientation and acceleration ✅  
   - C) Color  
   - D) Force  

3. Tactile sensors are mainly used for:  
   - A) Vision  
   - B) Touch and force feedback ✅  
   - C) Navigation  
   - D) Speech recognition  

4. Why is sensor calibration important?  
   - A) To make robot look better  
   - B) Ensure accurate measurements ✅  
   - C) Save energy  
   - D) None  

5. Proximity sensors prevent:  
   - A) Code errors  
   - B) Collisions ✅  
   - C) Slow movement  
   - D) None
