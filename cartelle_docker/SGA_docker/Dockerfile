# Usa come immagine di base una distribuzione Linux con GCC e CMake installati
FROM gcc:latest

# Installa CMake >=3.3
RUN apt-get update && \
    apt-get install -y cmake && \
    rm -rf /var/lib/apt/lists/*

# Scarica il repo
RUN git clone https://github.com/Mirkocoggi/SGA
# RUN git clone https://github.com/haowenz/SGA
# Crea e naviga nella directory di build
WORKDIR /SGA/extern
RUN rm -rf gfatools

RUN git clone https://github.com/lh3/gfatools.git
WORKDIR /SGA/extern/gfatools
RUN make
WORKDIR /SGA
RUN mkdir build
WORKDIR /SGA/build

# Configura la build di SGA
RUN cmake -DSGAL_BUILD_TESTING=ON ..

# Compila il progetto
RUN make

# Esegui i test
RUN ctest

RUN mkdir output
RUN mkdir input_data