#Tool for parsing the JSON file and creating the csv with node_id and the offset pof the first character of the query
#And sorting by name if it is an integer
import json
import csv

def extract_values(json_file):
    with open(json_file) as file_object:
        data = json.load(file_object)

    values = []
    i = 1
    name=""
    for line in data:
        if name != line['name']:
            node_id = line['path']['mapping'][0]['position']['node_id']
            if "offset" in line['path']['mapping'][0]['position']:
                offset = line['path']['mapping'][0]['position']['offset']
            else:
                offset = "0"
            if "name" in line:
                name = line['name']
            # print(str(i) + '\t' + node_id + '\t' + offset + '\t' + name)
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

def add_rows(csv_file_t, new_csv_file_t):

    with open(csv_file_t, "r") as pre_file:
        reader = list(csv.reader(pre_file))
        i=1
        print("list= " + str(len(reader)))
        for read in reader:
            # print("i = " + str(i))
            if read[0] != "node_id":
                
                print("read[2] = " + read[2] + " and i = " + str(i))
                if read[2] == str(i):
                    i += 1
                else :
                    if read[2] != str(i):
                        reader.insert(i, ("0", "0", str(i)))
                        i += 1
                        
                

    with open(new_csv_file_t, "w") as post_file:
        writer = csv.writer(post_file)
        for line in reader:
            writer.writerow(line)


json_file = 'results/GA_err/yeast.json'
csv_file = 'results/GA_err/csv/yeast_n.csv'
new_csv_file = 'results/GA_err/csv/yeast.csv'


values = extract_values(json_file)

save_to_csv(values, csv_file)

add_rows(csv_file, new_csv_file)


