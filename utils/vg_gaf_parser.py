import csv

import re

def save_to_csv(values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node_id', 'offset'])
        writer.writerows(values)

def sum_numbers_after_colon(cigar_cs):
    numbers = re.findall(r':(\d+)', cigar_cs)
    total = sum(map(int, numbers))
    return total
global_score = 0 
i = 0
gaf_file = 'results/long_err_vg/vg/MHC/f_MHC-57_alignments.gaf'
csv_file = 'results/long_err_vg/vg/position_csv/f_1k_err.csv'
with open(gaf_file, 'r') as f_in:
    with open(csv_file, 'w') as f_out:
        values_pos =[]
        for line in f_in:
            i=i+1
            print(i)
            if line.startswith('#'):
                continue
            values = line.strip().split('\t')
            if (values[2] == "*" or values[5] == "*"):
                node_id="0"
                offset="0"
            else:
                nodes = re.split(r'[><]', values[5].strip())
                node_id = nodes[1] 
                offset=values[7]

            if node_id is not None and offset is not None:
                values_pos.append((node_id, offset))
            
            # value = values[14]
            # cs_values = values[14].split('cs:Z:')
            # cs_value = cs_values[1]
            # total_score = int(values[1]) - sum_numbers_after_colon(cs_value)
            # global_score = global_score + total_score
            # csv_values = values[:12]
            # csv_values.append(cs_value)
            # writer.writerow(csv_values)

save_to_csv(values_pos, csv_file)
print("total score: ", global_score) 