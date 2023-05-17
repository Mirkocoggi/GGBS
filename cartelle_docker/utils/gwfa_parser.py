import csv

with open('output_gen/out/out_gwfa.log', 'r') as f:
    lines = f.readlines()

output = []
for line in lines:
    if not line.startswith('[gwf_ed]'):
        cost_str = line.split('\t')[1]
        output.append([int(cost_str)])

with open('results/out_gwfa.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Read Cost'])
    writer.writerows(output)