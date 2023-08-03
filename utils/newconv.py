#VG sim only works with clear GFA input, this tool was created to clean MHC-57.gfa because it had more info at the end of the line and vg sim couldn't parse it
file_path = 'ggbs/cartelle_docker/shared_input/graphs/f_MHC-57.gfa'

with open(file_path, 'r') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    if line.startswith('S'):
        line_parts = line.split('\t')
        print(line_parts[1])
        line_parts[1] = line_parts[1][1:]
        new_line = line_parts[0] + '\t' + line_parts[1] + '\t' + line_parts[2] + '\n'
        new_lines.append(new_line)
    elif line.startswith('L'):
        line_parts = line.split('\t')
        line_parts[1] = line_parts[1][1:]
        line_parts[3] = line_parts[3][1:]
        new_line = line_parts[0] + '\t' + line_parts[1] + '\t' + line_parts[2] + '\t' + line_parts[3] + '\t' + line_parts[4] + '\t' + line_parts[5] + '\n'
        new_lines.append(new_line)
    else:
        new_lines.append(line)

new_file_path = 'ggbs/cartelle_docker/shared_input/graphs/f_MHC-57_modified.gfa'
with open(new_file_path, 'w') as file:
    file.writelines(new_lines)