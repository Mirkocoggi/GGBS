input_file = "lievito.fq"
output_file = "lievito.fa"

with open(input_file, "r") as fq_file, open(output_file, "w") as fa_file:
    for line in fq_file:
        if line.startswith("@"):
            # Modify the line starting with "@"
            modified_line = ">" + line[1:]
            fa_file.write(modified_line)
        elif line.startswith("+") or line.startswith("2"):
            # Skip lines starting with "+" or "2"
            continue
        else:
            # Write lines with A, C, G, or T
            fa_file.write(line)