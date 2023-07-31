import yaml
import os
import shutil
from pathlib import Path

# Here are reported the templated Dockerfiles, for each tool
# If you want to update them, please pay attention in escaping brackets {{}} and backslashes \\
DOCKERFILES = {
	'GraphAligner' : '''\
FROM continuumio/miniconda3:latest

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/maickrau/GraphAligner.git
WORKDIR /GraphAligner
RUN git checkout {}
RUN git submodule update --init --recursive
RUN conda env create -f CondaEnvironment.yml
RUN echo "source activate GraphAligner" >> ~/.bashrc
ENV PATH /opt/conda/envs/GraphAligner/bin:$PATH
RUN apt-get update && apt-get install -y g++ && apt-get install -y make
RUN make bin/GraphAligner
ENV PATH /GraphAligner/bin:$PATH

CMD ["/bin/bash"]

RUN mkdir output
RUN mkdir input_data

    ''',

    'vg' : '''\
FROM mirror.gcr.io/library/ubuntu:20.04 AS base

RUN apt-get update && apt-get install -y git

RUN git clone --recursive https://github.com/vgteam/vg.git

WORKDIR /vg

RUN git checkout {}

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

FROM base AS build
ARG THREADS=8
ARG TARGETARCH

RUN apt-get -qq -y update && \\
    apt-get -qq -y upgrade && \\
    apt-get -qq -y install sudo

RUN apt-get -qq -y update && apt-get -qq -y upgrade && apt-get -qq -y install \\
    make git build-essential protobuf-compiler libprotoc-dev libjansson-dev libbz2-dev \\
    libncurses5-dev automake gettext autopoint libtool jq bsdmainutils bc rs parallel npm \\
    samtools curl unzip redland-utils librdf-dev cmake pkg-config wget gtk-doc-tools \\
    raptor2-utils rasqal-utils bison flex gawk libgoogle-perftools-dev liblz4-dev liblzma-dev \\
    libcairo2-dev libpixman-1-dev libffi-dev libcairo-dev libprotobuf-dev libboost-all-dev \\
    tabix bcftools libzstd-dev pybind11-dev python3-pybind11


RUN if [ -z "${{TARGETARCH}}" ] || [ "${{TARGETARCH}}" = "amd64" ] ; then sed -i s/march=native/march=nehalem/ deps/sdsl-lite/CMakeLists.txt; fi

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${{TARGETARCH}}" ] || [ "${{TARGETARCH}}" = "amd64" ] ; then echo " -march=nehalem "; fi)" CFLAGS="$(if [ -z "${{TARGETARCH}}" ] || [ "${{TARGETARCH}}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) deps

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${{TARGETARCH}}" ] || [ "${{TARGETARCH}}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) objs

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${{TARGETARCH}}" ] || [ "${{TARGETARCH}}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) static && strip -d bin/vg

ENV PATH /vg/bin:$PATH

RUN mkdir output
RUN mkdir input_data

    ''',

    'astarix': '''\
FROM ubuntu:20.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \\
		build-essential \\
		libc-dev \\
		python3 \\
		python3-pip \\
        git\\
        cmake\\
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/eth-sri/astarix
RUN git checkout {}

WORKDIR /astarix

RUN pip3 install pandas

# compile and test

RUN make && \\
	make test

RUN mkdir output
RUN mkdir input_data

    ''',

    'gwfa': '''\
FROM ubuntu:latest

RUN apt-get update && apt-get -y upgrade && apt-get -y install build-essential git zlib1g-dev

RUN git clone https://github.com/lh3/gwfa.git ./gwfa
WORKDIR ./gwfa

RUN git checkout {}
RUN make

RUN mkdir output
RUN mkdir input_data

    ''',

    'SGA': '''\
FROM gcc:latest

RUN apt-get update && \\
    apt-get install -y cmake && \\
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Mirkocoggi/SGA
# RUN git clone https://github.com/haowenz/SGA
WORKDIR /SGA/extern
RUN git checkout {}

RUN rm -rf gfatools
RUN git clone https://github.com/lh3/gfatools.git

WORKDIR /SGA/extern/gfatools
RUN make

WORKDIR /SGA
RUN mkdir build

WORKDIR /SGA/build
RUN cmake -DSGAL_BUILD_TESTING=ON ..
RUN make
RUN ctest
RUN cp apps ..

WORKDIR /SGA
RUN mkdir output
RUN mkdir input_data

    ''',

    'V-ALIGN': '''\
FROM gcc:latest

RUN git clone https://github.com/tcsatc/V-ALIGN
RUN git checkout {}

WORKDIR /V-ALIGN
RUN make

RUN mkdir output
RUN mkdir input_data

    '''
}


def main():
	
    # Open the tools_config.yml file and read tools' configuration
    with open('tools_config.yml', 'r') as file:
        config = yaml.safe_load(file)

    # Create the Dockerfiles folder, if it doesn't exist yet
    if not os.path.exists('Dockerfiles'):
        os.makedirs('Dockerfiles')

    # Select Dockerfiles as working directory
    DOCKERFILES_FOLDER = os.path.join(os.getcwd(), 'Dockerfiles')
    os.chdir(DOCKERFILES_FOLDER)

    # Eventually, remove previously existing folders
    folder_list = [f for f in Path(DOCKERFILES_FOLDER).glob('**/*') if not f.is_file()]
    for dir in folder_list: 
        shutil.rmtree(os.path.join(DOCKERFILES_FOLDER, dir))

    # Create subfolders in Dockerfiles, one for each tested tool
    for tool in config:
        os.makedirs(tool)

    # For each tool, create a Dockerfile in its subfolder
    for tool in config:
        os.chdir(os.path.join(DOCKERFILES_FOLDER, tool))
        file_tmp = open('Dockerfile', 'w')
        file_tmp.write(DOCKERFILES[tool].format(config[tool]['version']))
        file_tmp.close()

    # Print a success message
    print('\nSuccessfully created dockerfiles for the following tools:')
    for tool in config:
        print(f'\t{tool}')
    print()


if __name__ == '__main__':
	main()