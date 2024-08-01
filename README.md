# ROS2 Publisher and Subscriber Project

This repository contains a ROS2 project in which a Python publisher node -> simulating a gyroscope, and a C++ subscriber node -> simulating an altitude controller, communicate between each other. The publishing node will publish random data simulating a gyroscope's data every 10 seconds, which will in turn be received by the simulated altitude controller.

### Prerequisites
- ROS2 Humble 
- Python 3
- C++ compiler

## Steps
### Clone the Repository
```bash
git clone https://github.com/SophiaClifton/ros2_pubsub.git
cd ROS2_PubSub
```
### Build the Cloned Repository
```bash
cd src
colcon build
```
## In two seperate terminals: 
### Run the subscriber node
```bash
source install/setup.bash
ros2 run gyro_receiver listener
```
### Run the publisher node
```bash
source install/setup.bash
ros2 run gyro_publisher talker
```
