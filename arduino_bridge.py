# from https://github.com/Siddharth-Andhale/ROS2_Arduino_Bridge/blob/main/src/arduino_bridge.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class ArduinoBridge(Node):

    def __init__(self):
        super().__init__('arduino_bridge')
        self.ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1)
        time.sleep(2)  # Give time for Arduino to reset

        self.create_subscription(
            String,
            'sketch_nov2a',
            self.listener_callback,
            10
        )

        self.publisher_ = self.create_publisher(String, 'arduino_response', 10)

        self.timer = self.create_timer(0.1, self.read_from_arduino)

        self.get_logger().info('Arduino Bridge Node Started')

    def listener_callback(self, msg):
        command = msg.data
        self.ser.write(command.encode())
        self.get_logger().info('Command sent to Arduino: "%s"' % command)

    def read_from_arduino(self):
        if self.ser.in_waiting > 0:
            response = self.ser.readline()
            
            self.get_logger().info(f'Raw data received from Arduino: {response}')

def main(args=None):
    rclpy.init(args=args)
    node = ArduinoBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()