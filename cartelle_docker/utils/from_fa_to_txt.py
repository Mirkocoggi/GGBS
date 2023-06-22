
input_file = 'shared_input/input_data/reads_umane/C4-96.fa'
output_file = 'shared_input/input_data/reads_umane/C4-96.txt'
with open(input_file, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                if not line.startswith('>'):
                    output.write(line)


