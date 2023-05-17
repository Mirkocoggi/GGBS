import csv

with open('output_gen/out/out_valign.log', 'r') as f:
    lines = f.readlines()

output = []
for line in lines:
    if 'b) Alignment Score:' in line:
        cost_str = line.split(' ')[3]
        output.append([float(cost_str)])

with open('results/out_valign.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Read Cost'])
    writer.writerows(output)