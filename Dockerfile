FROM dustynv/ros:humble-ros-base-l4t-r32.7.1

WORKDIR /app

COPY arduino_bridge.py /app/arduino_bridge.py

RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install --no-cache-dir pyserial

CMD ["python", "/app/arduino_bridge.py"]
