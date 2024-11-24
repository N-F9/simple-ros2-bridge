# This bridge uses the ros 2 python library and pyserial to communicate between the jetson nano and an arduino.  

import rclpy # Documentation: https://docs.ros2.org/latest/api/rclpy/index.html
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

# A topic is a named bus where messages are passed from publishers to subscribers. There can be multiple of each in one topic.
# A publisher is a node that sends data to a particular topic. 
# A subscriber is a node that receives data from a topic. 

class ArduinoBridge(Node):
    def __init__(self):
        super().__init__('arduino_bridge')
        self.serial = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # Give time for Arduino to reset

        # Read in data serially.
        self.create_timer(
            timer_period_sec=1, 
            callback=self.read_from_arduino
        )

        # Manually publish with ros2 topic pub simple_arduino_bridge_subscriber_write std_msgs/String '{data: "o"}'
        # Good for debugging and figuring out what is wrong with a section of code.
        self.subscriber_write = self.create_subscription(
            msg_type=String, 
            topic='simple_arduino_bridge_subscriber_write', 
            callback=self.write_to_arduino, 
            qos_profile=10
        )

        # subscriber_publisher and publisher are in the same topic.
        # Publishers are useful when we want to send data to subscribers through code. We should prefer this method for production related funcationality.
        self.subscriber_publisher = self.create_subscription(
            msg_type=String, 
            topic='simple_arduino_bridge_publisher', 
            callback=self.write_to_arduino, 
            qos_profile=10
        )

        self.publisher = self.create_publisher(
            msg_type=String, 
            topic='simple_arduino_bridge_publisher',
            qos_profile=10
        )

        # Create a timer to publish a toggle message every 10 seconds
        self.timer = self.create_timer(
            timer_period_sec=10, 
            callback=self.toggle_led
        )

        self.get_logger().info('Arduino Bridge Node Started')
    
    def toggle_led(self):
        # create a message, with data of toggle
        msg = String()
        msg.data = "t"
        
        # publish this message to the topic
        self.publisher.publish(msg)
        
        # log that we just published a toggle
        self.get_logger().info(f'Publishing: "{msg.data}"')

    def write_to_arduino(self, msg):
        # read in the command
        command = msg.data

        # write serially to the arduino
        self.serial.write(command.encode())

        # log the command we sent to the arduino
        self.get_logger().info('Command sent to Arduino: "%s"' % command)
        
    def read_from_arduino(self):
        # clear the serial output line by line
        while self.serial.in_waiting > 0:
            # read in the line
            response = self.serial.readline()
            
            # log the line that we received from the arduino
            self.get_logger().info(f'Raw data received from Arduino: {response.decode("utf-8")}')

def main(args=None):
    # Initializes the bridge
    rclpy.init(args=args)
    node = ArduinoBridge()

    try:
        # Starts the bridge
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Ends the bridge
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()