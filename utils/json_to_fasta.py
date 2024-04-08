#Tool for converting the json output of the vg sim with the simulated reads in a FASTA file.
#ATTENTION!!!
#It could fail if the JSON file is not fixed. To repair the file I used https://josdejong.github.io/jsonrepair/
import json

def extract_values(json_file):
    with open(json_file) as file_object:
        data = json.load(file_object)

    values = []
    i = 1
    for line in data:
        sequence = line["sequence"]
        

        if sequence is not None:
            header = '>' + str(i)
            values.append(str(header))
            values.append(str(sequence))
            i = i + 1

    return values

def save_to_fasta(values, fasta_file):
    with open(fasta_file, 'w', newline='') as file:
        for value in values:
            file.write(value + '\n')

json_file = 'cov_guhi.json'
fasta_file = '100k_100bp_covid.fa'

values = extract_values(json_file)
save_to_fasta(values, fasta_file)