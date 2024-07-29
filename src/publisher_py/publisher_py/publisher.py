import rclpy
from geometry_msgs.msg import Quaternion
import random
import time

def main():
    rclpy.init() 
    node = rclpy.create_node("publishing_node")
    publisher = node.create_publisher(Quaternion, "publishing_topic", 10)

    while rclpy.ok():  # Keep asking as long as this node is running
        try:    
            x = random.uniform(-1, 1) #generate random coordinates rounded to 2 decimal places
            y = random.uniform(-1, 1)
            z = random.uniform(-1, 1)
            w = random.uniform(-1, 1)

            coordinates = Quaternion()
            coordinates.x = round(float(x), 2)
            coordinates.y = round(float(y), 2)
            coordinates.z = round(float(z), 2)
            coordinates.w = round(float(w), 2)
            print(coordinates) 
            publisher.publish(coordinates)
            time.sleep (10) # to avoid crashing my pc

        except KeyboardInterrupt: # program will shut done properly when Ctrl+C is pressed to terminate the program
            pass
    node.destroy_node()
    rclpy.shutdown()

''' #for manual input
    try:
        while rclpy.ok():  # Keep asking as long as this node is running
            try: #pccount for invalid input
                x = input("What's x? ")
                y = input("What's y? ")
                z = input("What's z? ")
                w = input("What's w? ")

                coordinates = Quaternion()
                coordinates.x = float(x)
                coordinates.y = float(y)
                coordinates.z = float(z)
                coordinates.w = float(w)

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