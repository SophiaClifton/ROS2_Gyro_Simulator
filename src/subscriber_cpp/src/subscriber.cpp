#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/quaternion.hpp"


class AttitudeControl_Listener : public rclcpp::Node
{
public:
  AttitudeControl_Listener() : Node("altitude_controller")
  {
    gyroscope_data_receiver = this->create_subscription<geometry_msgs::msg::Quaternion>(
      "gyroscope_data_publisher", 10, std::bind(&AttitudeControl_Listener::topic_callback, this, std::placeholders::_1));
  }

private:
  void topic_callback(const geometry_msgs::msg::Quaternion::SharedPtr msg)
  {
    RCLCPP_INFO(get_logger(), "Received data: x=%f, y=%f, z=%f, w=%f",
                msg->x, msg->y, msg->z, msg->w);
  }

  rclcpp::Subscription<geometry_msgs::msg::Quaternion>::SharedPtr gyroscope_data_receiver;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<AttitudeControl_Listener>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}