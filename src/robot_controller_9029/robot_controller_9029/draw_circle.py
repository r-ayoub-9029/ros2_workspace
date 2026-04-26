#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class draw_circle_node(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer1 = self.create_timer(1, self.send_velocity_cmd)
        self.get_logger().info("Draw Circle node has been started ^_^ ")



    def send_velocity_cmd(self):
        message = Twist()
        message.linear.x = 2.0
        message.angular.z = 1.8
        self.cmd_vel_pub.publish(message)




def main(args=None):
    rclpy.init(args=args)
    node = draw_circle_node()
    rclpy.spin(node)
    rclpy.shutdown()
