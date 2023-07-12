import csv

import re

def sum_numbers_after_colon(cigar_cs):
    numbers = re.findall(r':(\d+)', cigar_cs)
    total = sum(map(int, numbers))
    return total
global_score = 0 
i = 0
with open('output_gen/out/a_vg_n.gaf', 'r') as f_in:
    with open('results/vg_gaf.csv', 'w') as f_out:
        
        for line in f_in:
            i=i+1
            print(i)
            if line.startswith('#'):
                continue
            values = line.strip().split('\t')
            if values[2] == "*":
                continue
            value = values[13]
            cs_values = values[13].split('cs:Z:')
            cs_value = cs_values[1]
            total_score = int(values[1]) - sum_numbers_after_colon(cs_value)
            global_score = global_score + total_score
            # csv_values = values[:12]
            # csv_values.append(cs_value)
            # writer.writerow(csv_values)


print("total score: ", global_score) 