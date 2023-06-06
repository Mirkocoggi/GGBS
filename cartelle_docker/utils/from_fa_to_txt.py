
input_file = 'shared_input/input_data/SARS-CoV2.fa'
output_file = 'shared_input/input_data/SARS-CoV2.txt'
with open(input_file, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                if not line.startswith('>'):
                    output.write(line)


