---
title: Motors & Actuators
slug: /physical-ai-book/actuators
sidebar_label: Actuators
sidebar_position: 4
---

# Motors and Actuators in Robotics

Actuators are the **muscles of robots**. They convert electrical signals from controllers into **mechanical movement**, enabling robots to walk, grasp, or manipulate objects.

## Types of Actuators

1. **DC Motors**  
   - Provide rotational movement  
   - Used in wheels, joints, and simple robotic arms  

2. **Servo Motors**  
   - Precise angular control  
   - Used in arms, hands, and bipedal joints  

3. **Stepper Motors**  
   - Move in discrete steps  
   - Ideal for precise positioning  

4. **Linear Actuators**  
   - Produce linear motion  
   - Used in sliding mechanisms and height adjustment  

## Why Actuators Matter

- Enable robots to perform tasks and interact with the environment  
- Control movement for balance, walking, and object manipulation  
- Work in combination with sensors to achieve intelligent behavior  

## Learning Outcomes

By the end of this chapter, you will be able to:  
- Identify different types of actuators used in humanoid robotics  
- Explain how actuators convert electrical signals into movement  
- Understand motor control, torque, and speed requirements  
- Integrate actuators with sensors for smooth robotic operation  

## Practical Lab Exercise

**Objective:** Control a servo motor using Python.

**Steps:**  
1. Connect a servo motor to a microcontroller (e.g., Arduino or Jetson GPIO).  
2. Write a Python script to rotate the servo to specific angles.  
3. Execute the script and observe the servo movement.  
4. Combine with a sensor input (e.g., distance sensor) to move the servo automatically.

**Expected Output:**  
- Servo moves to programmed angles smoothly.  
- Sensor feedback modifies servo motion in real-time.

## Troubleshooting

1. **Motor not moving:** Check power supply and wiring.  
2. **Erratic movement:** Ensure PWM signals are correct and stable.  
3. **Overheating:** Avoid continuous high torque; use proper heat dissipation.

## Quiz (5 MCQs)

1. What is the main function of an actuator?  
   - A) Sense environment  
   - B) Convert electrical signals to movement ✅  
   - C) Store data  
   - D) Process AI algorithms  

2. Which motor allows precise angular control?  
   - A) DC Motor  
   - B) Servo Motor ✅  
   - C) Stepper Motor  
   - D) Linear Actuator  

3. Linear actuators produce:  
   - A) Rotational movement  
   - B) Linear motion ✅  
   - C) Oscillation  
   - D) Random motion  

4. Why is actuator-sensor integration important?  
   - A) To save code  
   - B) To allow smooth and intelligent movement ✅  
   - C) To reduce power usage  
   - D) None  

5. Stepper motors are ideal for:  
   - A) Continuous rotation  
   - B) Precise positioning ✅  
   - C) High-speed walking  
   - D) Touch sensing
