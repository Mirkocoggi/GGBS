FROM node:latest 

RUN apt-get update && apt-get install -y git

RUN git clone --recursive https://github.com/vgteam/vg.git
WORKDIR /vg

RUN apt-get update

# RUN apt-get install -y build-essential git cmake pkg-config libncurses5-dev libbz2-dev protobuf-compiler libprotobuf-dev libprotobuf-c-dev libjansson-dev automake autopoint libtool jq bsdmainutils bc rs parallel npm curl unzip redland-utils librdf-dev bison flex gawk liblzma-dev liblz4-dev libffi-dev libcairo2-dev libboost-all-dev libboost-graph-dev libzstd-dev
RUN apt-get install -y build-essential git cmake pkg-config libncurses5-dev libbz2-dev protobuf-compiler libprotobuf-dev libprotobuf-c-dev libjansson-dev automake autopoint libtool jq bsdmainutils bc rs parallel npm curl unzip redland-utils librdf-dev bison flex gawk liblzma-dev liblz4-dev libffi-dev libcairo2-dev libboost-all-dev libboost-graph-dev libzstd-dev pybind11-dev python3-pybind11
RUN . ./source_me.sh && make

ENV PATH="/vg/bin:${PATH}" 

RUN mkdir output
RUN mkdir input_data