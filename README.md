# ROS2 Publisher and Subscriber Project

This repository contains a ROS2 project in which a Python publisher node and a C++ subscriber node communicate between each other. The publisher node asks the user for coordinates and publishes them to a topic. The subscriber node listens to that topic, receives the coordinates, and then prints them.

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
ros2 run subscriber_cpp listener
```
### Run the publisher node
```bash
source install/setup.bash
ros2 run publisher_py talker
```
