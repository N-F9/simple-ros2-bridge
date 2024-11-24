FROM dustynv/ros:humble-ros-base-l4t-r32.7.1

WORKDIR /app

COPY *.py /app/

RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install --no-cache-dir pyserial

RUN apt-get install -y supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]