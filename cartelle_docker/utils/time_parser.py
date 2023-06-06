import os
import csv

directory = 'output_gen/time'
files = sorted(os.listdir(directory))

output = []
for filename in files:
    if filename.endswith(".log") and filename.startswith("a_"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if 'real' in line:
                time_str = line.split('\t')[-1]
                if 'm' in time_str and 's' in time_str:
                    minutes, seconds = time_str.split('m')
                    seconds = seconds[:-2]
                    output.append([int(minutes), float(seconds)])

with open('results/a_time.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Minutes', 'Seconds'])
    writer.writerows(output)

output = []
for filename in files:
    if filename.endswith(".log") and filename.startswith("b_"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if 'real' in line:
                time_str = line.split('\t')[-1]
                if 'm' in time_str and 's' in time_str:
                    minutes, seconds = time_str.split('m')
                    seconds = seconds[:-2]
                    output.append([int(minutes), float(seconds)])

with open('results/b_time.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Minutes', 'Seconds'])
    writer.writerows(output)