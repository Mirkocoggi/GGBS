import csv
import re

def save_to_csv(values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node_id', 'offset'])
        writer.writerows(values)

i = 0
gaf_file = 'results/results_dec/f_short_err/gedmap/MHC/f_MHC-57.sam'
csv_file = 'results/position_csv_geds/f_100_err.csv'

with open(gaf_file, 'r') as f_in:
    values_pos = []
    for line in f_in:
        i += 1
        print(i)
        if line.startswith('#'):
            continue
        values = line.strip().split('\t')
        if values[2] == "*" or values[5] == "*":
            read = values[0]
            node_id = "0"
            offset = "0"
        else:
            read = values[0]
            nodes = re.split(r'[:]', values[2].strip())
            node_id = nodes[1]
            offset = values[3]

        if node_id is not None and offset is not None and read is not None:
            values_pos.append((int(read), node_id, offset))

# Sort by the read column numerically
values_pos.sort(key=lambda x: x[0])

# Find the range of read values
min_read = 1
max_read = 10000

# Fill in missing read values
full_values_pos = []
seen_reads = set()
for value in values_pos:
    seen_reads.add(value[0])
    full_values_pos.append(value)

for read in range(min_read, max_read + 1):
    if read not in seen_reads:
        full_values_pos.append((read, '0', '0'))

# Sort again to ensure the new entries are in the correct order
full_values_pos.sort(key=lambda x: x[0])

# Remove duplicates based on the read column, keeping the first occurrence
unique_values_pos = []
seen_reads = set()
for value in full_values_pos:
    if value[0] not in seen_reads:
        seen_reads.add(value[0])
        unique_values_pos.append(value)

# Remove the read column
final_values_pos = [(node_id, offset) for _, node_id, offset in unique_values_pos]

# Save to CSV
save_to_csv(final_values_pos, csv_file)
