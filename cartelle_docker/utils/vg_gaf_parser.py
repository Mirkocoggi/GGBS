import csv

with open('output_gen/out_vg.gaf', 'r') as f_in:
    with open('results/vg_gaf.csv', 'w') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['read_id', 'read_length', 'offset', 'alignment_length', 'strand', 'query_name', 'query_length', 'query_start', 'query_end', 'target_start', 'target_end', 'quality_score', 'cigar_cs'])
        for line in f_in:
            if line.startswith('#'):
                continue
            values = line.strip().split('\t')
            cs_value = values[-2].split('cs:Z:')[1]
            csv_values = values[:12]
            csv_values.append(cs_value)
            writer.writerow(csv_values)