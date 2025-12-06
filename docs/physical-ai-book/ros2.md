---
title: ROS 2 Framework
slug: /physical-ai-book/ros2
sidebar_label: ROS 2
sidebar_position: 11
---

# ROS 2: Nodes, Topics, Services & Actions

In this chapter, we dive into the **Robot Operating System 2 (ROS 2)** framework. ROS 2 is the backbone of humanoid robotics, providing a **distributed, reliable, and modular architecture** for controlling robots.

## Learning Outcomes

Upon completing this chapter, you will be able to:  
- Understand ROS 2 architecture and its advantages over ROS 1  
- Implement **nodes, topics, services, and actions** in Python  
- Integrate AI agents with ROS 2 nodes for perception, planning, and control  
- Understand message passing and Quality of Service (QoS)  

## Core Concepts

### Nodes
- Nodes are independent processes that perform computation  
- Each functional unit (perception, planning, control) should be a separate node  

### Topics
- Topics allow asynchronous data streaming  
- Publishers send data, subscribers receive it  

### Services
- Synchronous request/response communication for short operations  
- Example: Resetting a sensor  

### Actions
- Long-running goals with feedback and cancellation support  
- Example: Move robot arm to a target position  

### DDS and QoS
- ROS 2 uses **Data Distribution Service (DDS)** for communication  
- QoS policies (reliability, durability, deadline) affect message behavior  

## Step-by-Step Implementation

1. Create a ROS 2 workspace  
2. Build packages for perception, planning, and control  
3. Implement a **Publisher Node** in Python to publish sensor data  

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = String()
        msg.data = 'Sensor reading'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
