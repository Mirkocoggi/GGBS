import csv

with open('output_gen/out/b_sga.log', 'r') as f:
    lines = f.readlines()

output = []
global_score = 0
for line in lines:
    if 'alignment cost:' in line:
        cost_str = line.split(' ')[4]
        cost_str=cost_str.split('cost:')[1]
        cost_str=cost_str.split(',')[0]
        output.append([cost_str])
        global_score = global_score + int(cost_str)

with open('results/out_sga.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Alignment Cost'])
    writer.writerows(output)

print("total score: ", global_score)