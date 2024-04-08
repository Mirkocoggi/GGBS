import csv

with open('results/2023_08_04_09_14_06/gwfa/yeast/d_yeast_alignments.json.log', 'r') as f:
    lines = f.readlines()

output = []
global_score = 0
for line in lines:
    if not line.startswith('[gwf_ed]'):
        cost_str = line.split('\t')[1]
        output.append([int(cost_str)])
        global_score = global_score + int(cost_str)

with open('results/out_gwfa.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Read Cost'])
    writer.writerows(output)

print("total score: ", global_score)