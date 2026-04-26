#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class listenerNode(Node):

    def __init__(self):
        super().__init__("listener")
        self.listen_ = self.create_subscription(Pose, "/turtle1/pose", self.pos_callback, 10)



    def pos_callback(self, message: Pose):
        self.get_logger().info("turtle pose -> X=" + str(message.x) + "Y=" + str(message.y) + "Theta=" + str(message.theta))




def main(args=None):
    rclpy.init(args=args)
    node = listenerNode()
    rclpy.spin(node)
    rclpy.shutdown()
