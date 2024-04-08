#Tool for parsing the JSON file and creating the csv with node_id and the offset pof the first character of the query
#And sorting by name if it is an integer
import json
import csv

def score_sum(json_file):
    with open(json_file) as file_object:
        data = json.load(file_object)
    sum=0
    for line in data:
        if "score" in line: 
            print("score: " + str(line['score']))
            sum = sum + line['score']
    return sum
        

json_file = 'results/GA_perfect/yeast.json'
sum = score_sum(json_file)
print("Total score sum: " + str(sum))





