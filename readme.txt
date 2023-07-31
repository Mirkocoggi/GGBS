1.  Select which tools and version you want to use in tools_config.yml

2.  Create a Dockerfiles folder that have a subfolder for each tool.
    In each subfolder there will be the respective Dockerfile.
    Run:
        python make_dockerfiles.py

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