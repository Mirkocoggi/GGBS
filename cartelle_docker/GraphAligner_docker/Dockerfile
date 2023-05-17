FROM continuumio/miniconda3:latest

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/maickrau/GraphAligner.git
WORKDIR /GraphAligner
RUN git submodule update --init --recursive
RUN conda env create -f CondaEnvironment_linux.yml
RUN echo "source activate GraphAligner" >> ~/.bashrc
ENV PATH /opt/conda/envs/GraphAligner/bin:$PATH
RUN apt-get update && apt-get install -y g++ && make bin/GraphAligner
ENV PATH /GraphAligner/bin:$PATH

CMD ["/bin/bash"]

RUN mkdir output
RUN mkdir input_data