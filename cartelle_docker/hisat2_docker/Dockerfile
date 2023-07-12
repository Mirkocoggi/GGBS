FROM ubuntu:20.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libc-dev python-is-python3 python3-pip git cmake

RUN git clone https://github.com/DaehwanKimLab/hisat2.git
WORKDIR /hisat2
RUN git checkout 5086938
RUN make


RUN mkdir output
RUN mkdir input_data