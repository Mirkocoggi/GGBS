# Genome Graphs Benchmark Suite - GGBS
GGBS is the first implemented Benchmark Suite for sequence-to-graph alignment in the genomic analysis context. It includes multiple state-of-the-art tools and six different genome graph built with VG Toolkit[^1]. Tools included are:

- Astarix [^2]
- GraphAligner [^3]
- GWFA [^4]
- SGA [^5]
- V-ALign [^6]
- VG Toolkit Giraffe [^7]


## Installation

### Install dependencies
Docker >= 24.0

### Download and install
First get the repo:
```
git clone https://github.com/Mirkocoggi/GGBS.git
```
Then just run:
```
cd GGBS
```

## Usage
After the installation, you can simply test it by running:
```
cd cartelle_docker
docker compose up
```
## Results Collection
Results are uploaded in the `/output_gen` folder. They are divided in `/time` and `/out`, collecting times and results respectively.

[^1]: E. Garrison, J. Sir ́en, A. M. Novak, G. Hickey, J. M. Eizenga, E. T. Dawson, W. Jones, S. Garg, C. Markello, M. F. Lin et al., “Variation graph toolkit improves read mapping by representing genetic variation in the reference,” Nature biotechnology, vol. 36, no. 9, pp. 875–879, 2018
[^2]: P. Ivanov, B. Bichsel, and M. Vechev, “Fast and optimal sequence-to-graph alignment guided by seeds,” in International Conference on Research in Computational Molecular Biology. Springer, 2022, pp. 306–325
[^3]: M. Rautiainen, V. M ̈akinen, and T. Marschall, “Bit-parallel sequence-to-graph alignment,” Bioinformatics, vol. 35, no. 19, 2019.
[^4]: H. Zhang, S. Wu, S. Aluru, and H. Li, “Fast sequence to graph alignment using the graph wavefront algorithm,” arXiv preprint arXiv:2206.13574, 2022.
[^5]: C. Jain, H. Zhang, Y. Gao, and S. Aluru, “On the complexity of sequence-to-graph alignment,” Journal of Computational Biology, vol. 27, no. 4, pp. 640–654, 2020.
[^6]: V. N. S. Kavya, K. Tayal, R. Srinivasan, and N. Sivadasan, “Sequence alignment on directed graphs,” Journal of Computational Biology, vol. 26, no. 1, pp. 53–67, 2019.
[^7]: J. Sir ́en, J. Monlong, X. Chang, A. M. Novak, J. M. Eizenga, C. Markello, J. A. Sibbesen, G. Hickey, P.-C. Chang, A. Carroll et al., “Genotyping common, large structural variations in 5,202 genomes using pangenomes, the giraffe mapper, and the vg toolkit,” BioRxiv, pp. 2020–12, 2020

