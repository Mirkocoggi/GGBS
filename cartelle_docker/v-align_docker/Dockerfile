FROM gcc:latest

RUN git clone https://github.com/tcsatc/V-ALIGN
WORKDIR /V-ALIGN
RUN make

RUN mkdir output
RUN mkdir input_data