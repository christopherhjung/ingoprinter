FROM ubuntu:18.04

RUN apt update
RUN apt install git -y
RUN git clone https://github.com/KevinOConnor/klipper
RUN bash ./klipper/scripts/install-ubuntu-18.04.sh
