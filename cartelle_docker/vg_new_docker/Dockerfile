FROM mirror.gcr.io/library/ubuntu:20.04 AS base

RUN apt-get update && apt-get install -y git

RUN git clone --recursive https://github.com/vgteam/vg.git

WORKDIR /vg

RUN git checkout a7b0f38

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

FROM base AS build
ARG THREADS=8
ARG TARGETARCH

RUN apt-get -qq -y update && \
    apt-get -qq -y upgrade && \
    apt-get -qq -y install sudo

RUN apt-get -qq -y update && apt-get -qq -y upgrade && apt-get -qq -y install \
    make git build-essential protobuf-compiler libprotoc-dev libjansson-dev libbz2-dev \
    libncurses5-dev automake gettext autopoint libtool jq bsdmainutils bc rs parallel npm \
    samtools curl unzip redland-utils librdf-dev cmake pkg-config wget gtk-doc-tools \
    raptor2-utils rasqal-utils bison flex gawk libgoogle-perftools-dev liblz4-dev liblzma-dev \
    libcairo2-dev libpixman-1-dev libffi-dev libcairo-dev libprotobuf-dev libboost-all-dev \
    tabix bcftools libzstd-dev pybind11-dev python3-pybind11


RUN if [ -z "${TARGETARCH}" ] || [ "${TARGETARCH}" = "amd64" ] ; then sed -i s/march=native/march=nehalem/ deps/sdsl-lite/CMakeLists.txt; fi

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${TARGETARCH}" ] || [ "${TARGETARCH}" = "amd64" ] ; then echo " -march=nehalem "; fi)" CFLAGS="$(if [ -z "${TARGETARCH}" ] || [ "${TARGETARCH}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) deps

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${TARGETARCH}" ] || [ "${TARGETARCH}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) objs

RUN . ./source_me.sh && CXXFLAGS="$(if [ -z "${TARGETARCH}" ] || [ "${TARGETARCH}" = "amd64" ] ; then echo " -march=nehalem "; fi)" make -j $((THREADS < $(nproc) ? THREADS : $(nproc))) static && strip -d bin/vg

ENV PATH /vg/bin:$PATH

RUN mkdir output
RUN mkdir input_data