FROM ubuntu:latest

# Aggiorna il sistema operativo e installa le dipendenze necessarie
RUN apt-get update && apt-get -y upgrade && apt-get -y install build-essential git zlib1g-dev

# Clona il repository del programma
RUN git clone https://github.com/lh3/gwfa.git /usr/local/gwfa

# Installa il programma
WORKDIR /usr/local/gwfa
RUN make

RUN mkdir output
RUN mkdir input_data