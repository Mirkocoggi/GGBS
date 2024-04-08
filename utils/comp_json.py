import csv
import pandas as pd

counter = 0

filename1 = "input_data/JSON/position/d_yeast_reads_err.csv"
filename2 = "results/GA_err/csv/yeast.csv"

df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)
df2.rename(columns={"node_id": "node_id2"}, inplace=True)
df2.rename(columns={"offset": "offset2"}, inplace=True)

merged_df = pd.concat([df1, df2], axis=1)

print(merged_df.head())

for i in range(10000):
    if merged_df.loc[i, 'node_id'] == merged_df.loc[i, 'node_id2'] and abs(int(merged_df.loc[i, 'offset']) - int(merged_df.loc[i, 'offset'])) < 10:
        counter+=1

print(f"The counter value is: {counter} over {len(df1.index)}")