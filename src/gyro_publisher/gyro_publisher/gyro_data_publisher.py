import rclpy
from geometry_msgs.msg import Quaternion
import random
import time

class Gyroscope:
    def __init__(self):
        rclpy.init() 
        self.gyro_pub_node = rclpy.create_node("gyro_pub_node")
        self.gyro_data_pub = self.gyro_pub_node.create_publisher(Quaternion, "gyro_data_pub", 10)

    def publish_data(self):   
        x = random.uniform(-1, 1) #generate random coordinates rounded to 2 decimal places
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)

        data = Quaternion()
        data.x = round(float(x), 2)
        data.y = round(float(y), 2)
        data.z = round(float(z), 2)
        data.w = 1.0

        self.gyro_pub_node.get_logger().info(
            f"Published data: x={data.x:.2f}, y={data.y:.2f}, z={data.z:.2f}, w={data.w:.2f}"
        )
        self.gyro_data_pub.publish(data)
        time.sleep (10) # to avoid crashing my pc

    def spin(self):
        try:
            while rclpy.ok():  # Keep asking as long as this node is running
                self.publish_data()
                time.sleep(10)
                
        except KeyboardInterrupt: # program will shut done properly when Ctrl+C is pressed to terminate the program
                pass

    def destroy(self):
        self.gyro_pub_node.destroy_node()
        rclpy.shutdown()

def main():
    gyroscope = Gyroscope()
    gyroscope.spin()
    gyroscope.destroy()

if __name__ == '__main__':
    main()
