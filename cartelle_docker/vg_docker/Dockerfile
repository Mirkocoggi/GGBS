FROM node:latest 

RUN apt-get update && apt-get install -y git


RUN git clone --recursive https://github.com/vgteam/vg.git

WORKDIR /vg

RUN apt-get update

# RUN apt-get install -y build-essential git cmake pkg-config libncurses5-dev libbz2-dev protobuf-compiler libprotobuf-dev libprotobuf-c-dev libjansson-dev automake autopoint libtool jq bsdmainutils bc rs parallel npm curl unzip redland-utils librdf-dev bison flex gawk liblzma-dev liblz4-dev libffi-dev libcairo2-dev libboost-all-dev libboost-graph-dev libzstd-dev
RUN apt-get install -y build-essential git cmake pkg-config libncurses5-dev libbz2-dev protobuf-compiler libprotobuf-dev libprotobuf-c-dev libjansson-dev automake autopoint libtool jq bsdmainutils bc rs parallel npm curl unzip redland-utils librdf-dev bison flex gawk liblzma-dev liblz4-dev libffi-dev libcairo2-dev libboost-all-dev libboost-graph-dev libzstd-dev pybind11-dev python3-pybind11
# RUN git submodule update --init --recursive \
#     && git submodule sync \
#     && git submodule update --init --recursive
RUN git checkout b183e0e79c5babcb7748553bc1f7bb60b1957165
#1.49 : 276aa51e35f5b0e496c5092d753a2487cc6073f8 Giugno
#1.48 : f478c7f2ca14a7f971313804fb149d9f366655b9 Maggio 
#1.47 : d577e3d79c640dcbfc98d9e93b03de1b733abc2b Marzo
#1.46 : ceed9d3c744ff84ec7cf00499e681e16e9a6927f
#1.45 : 8570100f0945d6c3d0851c5da2feaf19d492f14d
#1.44 : 8e14f9e43219ff7389cb197c340a8a8e4613f87e
#1.43 : de51eb534394bb93a406baa809ac079ed2223eeb
RUN . ./source_me.sh && make

ENV PATH="/vg/bin:${PATH}" 

RUN mkdir output
RUN mkdir input_data