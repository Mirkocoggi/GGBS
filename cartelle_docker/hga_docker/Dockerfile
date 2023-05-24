FROM ubuntu:20.04

# Installa le dipendenze necessarie per l'installazione di CUDA
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    curl \
    ca-certificates
RUN apt-get install -y libxml2 
RUN apt-get install -y git
RUN apt-get install -y cmake
RUN apt-get install -y wget
RUN apt-get update && apt-get install -y g++

# Scarica e installa CUDA
RUN wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
#COPY cuda_11.8.0_520.61.05_linux.run .
RUN sh cuda_11.8.0_520.61.05_linux.run --silent --toolkit --override

# Imposta le variabili d'ambiente necessarie per l'utilizzo di CUDA
ENV PATH=/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}

# Rimuove il file di installazione CUDA
RUN rm cuda_11.8.0_520.61.05_linux.run


RUN git clone https://github.com/Mirkocoggi/hga
WORKDIR /hga
RUN make all
RUN make debug

RUN mkdir output
RUN mkdir input_data

# FROM nvidia/cuda:11.8.0-base-ubuntu20.04

# # RUN echo "Europe/Rome" > /etc/timezone
# ARG DEBIAN_FRONTEND=noninteractive


# RUN apt-get update && apt-get install -y --no-install-recommends \
#     git \
#     cmake \
#     g++ \
#     tzdata \
#     make \
#     nvidia-driver-470

# RUN git clone https://github.com/RapidsAtHKUST/hga
# WORKDIR /hga
# RUN make all
# RUN make debug

# RUN mkdir output
# RUN mkdir input_data
