# Genome Graphs Benchmark Suite - GGBS
GGBS is the first implemented Benchmark Suite for sequence-to-graph alignment in the genomic analysis context. It includes multiple state-of-the-art tools and six different genome graphs built with VG Toolkit[^1]. Tools included are:

- Astarix [^2]
- GraphAligner [^3]
- GWFA [^4]
- SGA [^5]
- V-ALign [^6]
- VG Toolkit Giraffe [^7]

Select which tools and version you want to use in tools_config.yml



3.  The folder INPUT_DATA contains genome graphs and sequence reads to be aligned.
    Each alignment experiment has its own folder, comprising two subfloders: 
    - GRAPH: contains the input graph in GFA format
    - READS: contains the sequence reads in FASTA/Q format
    The experiments' folders are grouped in two higher-level folders:
    - TEST: contains the alignments to be executed with the previously selected tools
    - IGNORE: contains alignment experiments we do not want to include in our evaluation

4. Create the docker-compose.yml that builds all the docker images and executes all the experiments.
    Run:
        python make_dockercompose.py

5. Run the experiments with the command:
        docker compose up

6. Results are in RESULTS









## Installation

### Install dependencies
Docker >= 24.0

### Download and install
First, get the repo:
```
git clone https://github.com/Mirkocoggi/GGBS.git
```
Then just run:
```
cd GGBS
```

## Usage

### Create the dockerfiles

Create a Dockerfiles folder containing a subfolder for each tool.
In each subfolder, there will be the respective Dockerfile.
Run:
```
        python make_dockerfiles.py
```

### Data Selection

The folder `input_data` contains genome graphs and sequence reads to be aligned.
Each alignment experiment has its folder, comprising two subfolders: 
  - `GRAPH`: contains the input graph in GFA format;
  - `READS`: contains the sequence reads in FASTA/Q format.
The experiments' folders are grouped into two higher-level folders:
  - `TEST`: contains the alignments to be executed with the previously selected tools;
  - `IGNORE`: contains alignment experiments that should not be included in the evaluation.

### Create docker compose file

Create the `docker-compose.yml` that builds all the docker images and executes all the experiments.
Run:
```
        python make_dockercompose.py
```
### Run the experiments
Run the experiments with the command:
```       
        docker compose up
``` 

## Results Collection
Results are uploaded in the `results` folder.

[^1]: E. Garrison, J. Sir ́en, A. M. Novak, G. Hickey, J. M. Eizenga, E. T. Dawson, W. Jones, S. Garg, C. Markello, M. F. Lin et al., “Variation graph toolkit improves read mapping by representing genetic variation in the reference,” Nature biotechnology, vol. 36, no. 9, pp. 875–879, 2018
[^2]: P. Ivanov, B. Bichsel, and M. Vechev, “Fast and optimal sequence-to-graph alignment guided by seeds,” in International Conference on Research in Computational Molecular Biology. Springer, 2022, pp. 306–325
[^3]: M. Rautiainen, V. M ̈akinen, and T. Marschall, “Bit-parallel sequence-to-graph alignment,” Bioinformatics, vol. 35, no. 19, 2019.
[^4]: H. Zhang, S. Wu, S. Aluru, and H. Li, “Fast sequence to graph alignment using the graph wavefront algorithm,” arXiv preprint arXiv:2206.13574, 2022.
[^5]: C. Jain, H. Zhang, Y. Gao, and S. Aluru, “On the complexity of sequence-to-graph alignment,” Journal of Computational Biology, vol. 27, no. 4, pp. 640–654, 2020.
[^6]: V. N. S. Kavya, K. Tayal, R. Srinivasan, and N. Sivadasan, “Sequence alignment on directed graphs,” Journal of Computational Biology, vol. 26, no. 1, pp. 53–67, 2019.
[^7]: J. Sir ́en, J. Monlong, X. Chang, A. M. Novak, J. M. Eizenga, C. Markello, J. A. Sibbesen, G. Hickey, P.-C. Chang, A. Carroll et al., “Genotyping common, large structural variations in 5,202 genomes using pangenomes, the giraffe mapper, and the vg toolkit,” BioRxiv, pp. 2020–12, 2020

