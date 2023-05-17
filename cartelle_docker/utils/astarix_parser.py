import csv

with open('output_gen/out/out_astarix.log', 'r') as f:
    lines = f.readlines()

output = []
for line in lines:
    if 'Total cost of aligned reads:' in line:
        cost_str = line.split(' ')[5]
        cost_str=cost_str.split(',')[0]
        output.append([int(cost_str)])

with open('results/out_astarix.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Total Cost'])
    writer.writerows(output)