#Tool for parsing the JSON file and creating the csv with node_id and the offset pof the first character of the query
import json
import csv

def extract_values(json_file):
    with open(json_file) as file_object:
        data = json.load(file_object)

    values = []
    i = 1
    for line in data:
        node_id = line['path']['mapping'][0]['position']['node_id']
        if "offset" in line['path']['mapping'][0]['position']:
            offset = line['path']['mapping'][0]['position']['offset']
        else:
            offset = "0"
        print(str(i) + '\t' + node_id + '\t' + offset)
        i = i + 1

        if node_id is not None and offset is not None:
            values.append((node_id, offset))

    return values

def save_to_csv(values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node_id', 'offset'])
        writer.writerows(values)

json_file = 'b_cov_reads_err4k_50.json'
csv_file = 'outputcov.csv'

values = extract_values(json_file)
save_to_csv(values, csv_file)