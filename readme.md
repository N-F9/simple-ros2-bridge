# Simple ROS2 Bridge

A simple ROS2 bridge to turn a LED on, off, and toggle.

Credits for the original bridge: https://github.com/Siddharth-Andhale/ROS2_Arduino_Bridge

On the docker container in one terminal:

- `sudo docker run --rm -it --runtime nvidia --network host --gpus all --device=/dev/ttyACM0 -e DISPLAY dustynv/ros:humble-ros-base-l4t-r32.7.1`  
- `sudo docker cp arduino_bridge.py {docker_id}:/arduino_bridge.py`  
- `pip install pyserial`   
- `python arduino_bridge.py`  

In another terminal:  

- `sudo docker exec -it {docker_id} bash`  
- `source /opt/ros/humble/install/setup.bash`  
- `ros2 topic pub {topic} std_msgs/String '{data: "o"}'`  
- `ros2 topic pub {topic} std_msgs/String '{data: "f"}'`  
- `ros2 topic pub {topic} std_msgs/String '{data: "t"}'`  

