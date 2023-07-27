# Genome Graphs Benchmark Suite - GGBS
GGBS is the first implemented Benchmark Suite for sequence-to-graph alignment in the genomic analysis context. It includes multiple state-of-the-art tools and six different genome graph built with VG Toolkit[^1].
Run in `/cartelle_docker` with 



## Installation

### Install dependencies
Docker >= 24.0

### Download and install
First get the repo:
```
git clone 
```
Then just run:
```
cd SGA && mkdir build && cd build
cmake -DSGAL_BUILD_TESTING=ON ..
make
```
This will build the tests. Then the tests can be run:
```
ctest
```

## Usage
SGA is a header only C++ library. It supports loading graphs in txt format and sequence files in fasta/q format. You can easily use its API to build your own applications. An example on how to use the library to align sequences to graphs is given. After the installation, you can simply test it by running:
```
./sga_example graph_file read_file
```

```
docker compose up
```

[^1]: E. Garrison, J. Sir ́en, A. M. Novak, G. Hickey, J. M. Eizenga, E. T. Dawson, W. Jones, S. Garg, C. Markello, M. F. Lin et al., “Variation graph toolkit improves read mapping by representing genetic variation in the reference,” Nature biotechnology, vol. 36, no. 9, pp. 875–879, 2018
