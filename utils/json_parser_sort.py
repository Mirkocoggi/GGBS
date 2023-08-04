#Tool for parsing the JSON file and creating the csv with node_id and the offset pof the first character of the query
#And sorting by name if it is an integer
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
        if "name" in line:
            name = line['name']
        else:
            name = "0"
        print(str(i) + '\t' + node_id + '\t' + offset + '\t' + name)
        i = i + 1

        if node_id is not None and offset is not None:
            values.append((node_id, offset, name))
        values = sorted(values, key=lambda x: int(x[2])) 

    return values

def save_to_csv(values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node_id', 'offset', 'name'])
        writer.writerows(values)

json_file = 'GA_test.json'
csv_file = 'GA_test.csv'

values = extract_values(json_file)

save_to_csv(values, csv_file)

