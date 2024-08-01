#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/quaternion.hpp"


class AltitudeController : public rclcpp::Node
{
public:
  AltitudeController() : Node("gyro_sub_node")
  {
    gyro_data_sub = this->create_subscription<geometry_msgs::msg::Quaternion>(
      "gyro_data_pub", 10, std::bind(&AltitudeController::gyroDataCallback, this, std::placeholders::_1));
  }

private:
  void gyroDataCallback(const geometry_msgs::msg::Quaternion::SharedPtr msg)
  {
    RCLCPP_INFO(get_logger(), "Received data: x=%f, y=%f, z=%f, w=%f",
                msg->x, msg->y, msg->z, msg->w);
  }

  rclcpp::Subscription<geometry_msgs::msg::Quaternion>::SharedPtr gyro_data_sub;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto altitude_controller = std::make_shared<AltitudeController>();
  rclcpp::spin(altitude_controller);
  rclcpp::shutdown();
  return 0;
}
