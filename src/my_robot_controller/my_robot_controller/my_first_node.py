import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # This is the "Message Type" for movement

class TurtleController(Node):
    def __init__(self):
        # 1. Name the node
        super().__init__('turtle_controller_node')
        
        # 2. Create a Publisher
        # We publish to '/turtle1/cmd_vel', using Twist messages, with a queue size of 10
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # 3. Create a Timer
        # This tells the code to run the 'send_velocity' function every 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_velocity)
        self.get_logger().info("Turtle Controller has started!")

    def send_velocity(self):
        msg = Twist()
        msg.linear.x = 2.0  # Move forward
        msg.angular.z = 1.0 # Turn left (this creates a circle)
        
        # 4. Actually send the message
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node) # Keeps the node running until you hit Ctrl+C
    rclpy.shutdown()

if __name__ == '__main__':
    main()
