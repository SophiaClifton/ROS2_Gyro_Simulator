#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/quaternion.hpp"


class ListenerNode : public rclcpp::Node
{
public:
  ListenerNode() : Node("listener_node")
  {
    subscription_ = this->create_subscription<geometry_msgs::msg::Quaternion>(
      "publishing_topic", 10, std::bind(&ListenerNode::topic_callback, this, std::placeholders::_1));
  }

private:
  void topic_callback(const geometry_msgs::msg::Quaternion::SharedPtr msg)
  {
    RCLCPP_INFO(get_logger(), "Received Quaternion: x=%f, y=%f, z=%f, w=%f",
                msg->x, msg->y, msg->z, msg->w);
  }

  rclcpp::Subscription<geometry_msgs::msg::Quaternion>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<ListenerNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}