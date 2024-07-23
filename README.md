# ROS2 Publisher and Subscriber

This repository contains a ROS2 project with a Python publisher and a C++ subscriber. The publisher node asks the user for coordinates and publishes them to a topic. The subscriber node listens to that topic, receives the coordinates, and then publishes them.

### Prerequisites
- ROS2 Humble 
- Python 3
- C++ compiler

### Clone the Repository
git clone https://github.com/SophiaClifton/ros2_pubsub.git
cd ROS2_PubSub

### How to build cloned repo
cd src
colcon build

## In two sperate terminals: 
### How to run the subscriber node
source install/setup.bash
ros2 run subscriber_cpp listener

### How to run the publisher node
source install/setup.bash
ros2 run publisher_py talker
