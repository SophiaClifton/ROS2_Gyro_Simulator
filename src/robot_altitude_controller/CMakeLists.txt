cmake_minimum_required(VERSION 3.5)
project(robot_altitude_controller)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(listener src/gyro_data_receiver.cpp)
ament_target_dependencies(listener rclcpp geometry_msgs)

install(TARGETS
  listener
  DESTINATION lib/${PROJECT_NAME})

ament_package()
