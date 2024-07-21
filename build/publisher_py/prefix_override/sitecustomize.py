import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sophia/Documents/GitHub/ROS2_PubSub/install/publisher_py'
