import csv
import pandas as pd

counter = 0
filename1 = "input_data/JSON/position/e_C490_reads.csv"
filename2 = "results/GA_perfect/csv/C4.csv"

with open(filename1) as file1, open(filename2) as file2:
    # reader1 = csv.DictReader(file1)
    # reader2 = csv.DictReader(file2)
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)

    merged_df = pd.merge(df1, df2, on='merge_key', how='left')

    # for row1 in reader1:
    #     for row2 in reader2:
    #         if row1['node_id'] == row2['node_id'] and abs(int(row1['offset']) - int(row2['offset'])) < 10:
    #             counter += 1
        # file2.seek(0)  # Reset the second file pointer back to the beginning
    for i in range(10000):
        if reader1[i][1] == reader2[i][1] and abs(int(reader1[i][2]) - int(reader2[i][2])) < 10:
            counter += 1

print(f"The counter value is: {counter}")