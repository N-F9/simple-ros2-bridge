# Simple ROS2 Bridge

A simple ROS2 bridge to turn a LED on, off, and toggle.

Credits for the original bridge: https://github.com/Siddharth-Andhale/ROS2_Arduino_Bridge

## Running The Bridge

On the docker container in one terminal:

- `sudo docker build -t arduino-bridge .`
- `sudo docker run -d --rm -it --runtime nvidia --network host --gpus all --device=/dev/ttyACM0 -e DISPLAY --name arduino-bridge-container arduino-bridge`
- `sudo docker ps`, to view if the container is running.
- `sudo docker logs arduino-bridge-container`, to view logs.
- `sudo docker stop arduino-bridge-container`, to stop the container.

In another terminal:  

- `sudo docker exec -it {docker_id} bash`  
- `source /opt/ros/humble/install/setup.bash`  
- `ros2 topic pub {topic} std_msgs/String '{data: "o"}'`  
- `ros2 topic pub {topic} std_msgs/String '{data: "f"}'`  
- `ros2 topic pub {topic} std_msgs/String '{data: "t"}'`  

## Things I Need To Do

- Simplify the above commands and setup by creating a new docker container image.
