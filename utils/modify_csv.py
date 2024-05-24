import csv

def modify_node_id(input_csv, output_csv):
    modified_rows = []
    
    # Read the input CSV file
    with open(input_csv, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        for row in reader:
            node_id = row[0]
            offset = row[1]
            modified_node_id = f"10{node_id}"
            modified_rows.append([modified_node_id, offset])
    
    # Write the modified data to the output CSV file
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(modified_rows)

# Define input and output CSV file paths
input_csv = 'results/position_csv_geds/a_100.csv'
output_csv = 'results/position_csv_geds/a_100.csv'

# Call the function to modify node_id and save the modified CSV
modify_node_id(input_csv, output_csv)
