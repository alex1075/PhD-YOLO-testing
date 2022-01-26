FROM tensorflow/tensorflow:latest
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade wheel
RUN apt install git curl wget -y
# RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0-py3-none-any.whl
COPY code/ /home/
COPY requirements.txt home/
COPY yolo* /home/
COPY data.names /home/
RUN mkdir /home/data
RUN cd /home && python3 -m pip install -r requirements.txt
CMD ["bash"]
