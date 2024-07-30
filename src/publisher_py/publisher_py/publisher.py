import rclpy
from geometry_msgs.msg import Quaternion
import random
import time

def main():
    rclpy.init() 
    random_gyroscope_publisher = rclpy.create_node("random_gyroscope_publisher")
    gyroscope_data_publisher = random_gyroscope_publisher.create_publisher(Quaternion, "gyroscope_data_publisher", 10)

    while rclpy.ok():  # Keep asking as long as this node is running
        try:    
            x = random.uniform(-1, 1) #generate random coordinates rounded to 2 decimal places
            y = random.uniform(-1, 1)
            z = random.uniform(-1, 1)

            data = Quaternion()
            data.x = round(float(x), 2)
            data.y = round(float(y), 2)
            data.z = round(float(z), 2)
            data.w = 1.0

            print(data) 
            gyroscope_data_publisher.publish(data)
            time.sleep (10) # to avoid crashing my pc

        except KeyboardInterrupt: # program will shut done properly when Ctrl+C is pressed to terminate the program
            pass
    random_gyroscope_publisher.destroy_node()
    rclpy.shutdown()

''' #for manual input
    try:
        while rclpy.ok():  # Keep asking as long as this node is running
            try: #pccount for invalid input
                x = input("What's x? ")
                y = input("What's y? ")
                z = input("What's z? ")

                coordinates = Quaternion()
                coordinates.x = float(x)
                coordinates.y = float(y)
                coordinates.z = float(z)
                coordinates.w = 1.0

                print(coordinates) 
                publisher.publish(coordinates)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
    except KeyboardInterrupt: # program will shut done properly when Ctrl+C is pressed to terminate the program
        pass

    node.destroy_node()
    rclpy.shutdown()
'''

if __name__ == '__main__':
    main()