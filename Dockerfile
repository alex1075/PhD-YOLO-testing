FROM ubuntu:latest
RUN apt update && apt update
RUN apt install -y python3 python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade wheel
RUN apt install git curl wget -y
RUN pip install tensorflow-macos==2.70  # for macOS
RUN pip install tensorflow-metal==0.3.0
COPY * /code
RUN cd /code && python3 -m pip install -r requirements.txt
