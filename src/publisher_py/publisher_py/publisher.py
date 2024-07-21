import rclpy
from geometry_msgs.msg import Quaternion

def main():
    rclpy.init() 
    node = rclpy.create_node("publishing_node")
    publisher = node.create_publisher(Quaternion, "publishing_topic", 10)

    try:
        while rclpy.ok():  # Keep asking as long as this node is running
            x = input("What's x? ")
            y = input("What's y? ")
            z = input("What's z? ")
            w = input("What's w? ")

            coordinates = Quaternion()
            coordinates.x = float(x)
            coordinates.y = float(y)
            coordinates.z = float(z)
            coordinates.w = float(w)

            print(coordinates) # for visualization
            publisher.publish(coordinates)

    except KeyboardInterrupt: # program will shut done properly when Ctrl+C is pressed to terminate the program
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()