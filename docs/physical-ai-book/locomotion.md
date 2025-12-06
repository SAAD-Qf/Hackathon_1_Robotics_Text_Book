---
title: Locomotion & Walking
slug: /physical-ai-book/locomotion
sidebar_label: Locomotion
sidebar_position: 5
---

# Locomotion and Walking in Humanoid Robots

Locomotion is how a humanoid robot **moves from one place to another**. It combines **actuation, balance, sensors, and control algorithms** to achieve walking, running, or dynamic movements.

## Types of Locomotion

1. **Bipedal Walking**  
   - Two-legged movement like humans  
   - Requires precise balance and weight distribution  

2. **Quadrupedal Walking**  
   - Four-legged robots for stability  
   - Used in rescue and exploration robots  

3. **Omnidirectional Movement**  
   - Can move in any direction without rotating  
   - Often used in wheeled humanoids or robots on wheels  

## Key Concepts

- **Center of Mass (CoM):** Helps maintain balance during movement  
- **Zero Moment Point (ZMP):** Critical for bipedal stability  
- **Gait Planning:** Sequence of steps and leg movements to walk naturally  
- **Inverse Kinematics:** Calculates joint angles to achieve desired foot positions  

## Learning Outcomes

By the end of this chapter, you will be able to:  
- Explain the principles of humanoid locomotion  
- Understand bipedal vs quadrupedal walking dynamics  
- Apply ZMP and gait planning concepts  
- Implement basic locomotion algorithms in Python or ROS 2  

## Practical Lab Exercise

**Objective:** Simulate bipedal walking in Gazebo or Unity.

**Steps:**  
1. Create a humanoid robot model in URDF/Xacro.  
2. Configure joints and actuators for legs.  
3. Implement a simple walking algorithm using ROS 2 nodes.  
4. Observe balance, CoM, and ZMP during the simulation.  
5. Adjust joint speeds and gait parameters to improve stability.  

**Expected Output:**  
- Humanoid robot moves forward with a stable gait  
- Balance maintained using CoM and ZMP adjustments  

## Troubleshooting

1. **Robot falls frequently:** Check gait parameters and CoM calculation  
2. **Leg joints do not move:** Ensure actuators are correctly mapped in URDF  
3. **Unnatural walking:** Fine-tune joint velocities and step lengths  

## Quiz (5 MCQs)

1. What is ZMP in humanoid robotics?  
   - A) Zone of Motion Prediction  
   - B) Zero Moment Point ✅  
   - C) Zoom Motion Parameter  
   - D) Zero Movement Position  

2. Bipedal walking requires:  
   - A) High torque only  
   - B) Precise balance and gait planning ✅  
   - C) Wheels  
   - D) None  

3. CoM stands for:  
   - A) Center of Mass ✅  
   - B) Control of Motion  
   - C) Coordinates of Movement  
   - D) Central Motor  

4. Which is more stable by default?  
   - A) Bipedal  
   - B) Quadrupedal ✅  
   - C) Unipedal  
   - D) Tripedal  

5. Inverse Kinematics is used to:  
   - A) Move sensors  
   - B) Calculate joint angles for desired positions ✅  
   - C) Control battery usage  
   - D) Detect obstacles
