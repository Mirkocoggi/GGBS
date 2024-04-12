input_file = "d_yeast_reads.fa"
output_file = "d_yeast_reads.fq"

with open(input_file, "r") as fa_file, open(output_file, "w") as fq_file:
    for line in fa_file:
        if line.startswith(">"):
            # Modify the line starting with "@"
            modified_line = "@" + line[1:]
            fq_file.write(modified_line)
        else:
            # Write lines with A, C, G, or T
            fq_file.write(line)
            fq_file.write('+\n')
            fq_file.write('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222\n')
