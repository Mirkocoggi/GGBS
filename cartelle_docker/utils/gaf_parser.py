

import csv
import re

# Split cigar string and calculate total score
def calculate_score(cigar_str):
    symbols = ['=', 'X', 'D', 'I']
    scores = [0, 1, 1, 1]
    tokens = re.findall(r'(\d+)([{}])'.format(''.join(symbols)), cigar_str)
    total_score = 0
    for token in tokens:
        num = int(token[0])
        sym = token[1]
        score = scores[symbols.index(sym)]
        total_score += num * score
    return total_score


with open('output_gen/out/out_GA.gaf', 'r') as f_in:
    with open('results/aln_GA.csv', 'w') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['read_id', 'read_length', 'offset', 'alignment_length', 'strand', 'query_name', 'query_length', 'query_start', 'query_end', 'target_start', 'target_end', 'quality_score', 'cigar', 'score'])
        for line in f_in:
            if line.startswith('#'):
                continue
            values = line.strip().split('\t')
            attribute = ''
            for i in range(11, len(values)):
                if values[i].startswith('NM'):
                    break
                attribute += values[i] 
            last_string = values[-1].split('cg:Z:')[1]
            total_score = calculate_score(last_string)
            csv_values = values[:11]
            csv_values.append(attribute)
            csv_values.append(last_string)
            csv_values.append(total_score)
            writer.writerow(csv_values)




