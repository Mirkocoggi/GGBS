import os
import pandas as pd

# Define the paths to the two folders
folder1 = 'results/position_csv_ga'
folder2 = 'zip_reads_folder/position_csv'

# Get the list of CSV files in both folders
files1 = [f for f in os.listdir(folder1) if f.endswith('.csv')]
files2 = [f for f in os.listdir(folder2) if f.endswith('.csv')]

# Ensure both folders contain the same files
if set(files1) != set(files2):
    raise ValueError("The folders do not contain the same set of CSV files")

# Initialize a list to store the results
results = []

# Iterate through each file in the folders
for file in files1:
    # Read the CSV files
    df1 = pd.read_csv(os.path.join(folder1, file))
    df2 = pd.read_csv(os.path.join(folder2, file))

    # Ensure both DataFrames have the same number of rows
    if len(df1) != len(df2):
        raise ValueError(f"The CSV files {file} do not have the same number of rows")

    # Initialize the counter
    counter = 0

    # Iterate through the rows of the DataFrames
    for i in range(len(df1)):
        node_id1 = df1.iloc[i, 0]
        node_id2 = df2.iloc[i, 0]
        offset1 = df1.iloc[i, 1]
        offset2 = df2.iloc[i, 1]

        # Check if node_ids are the same
        if node_id1 == node_id2:
            # Check the offset difference
            if abs(offset1 - offset2) < 10:
                counter += 1

    # Append the result to the list
    normalized_counter = counter / len(df1)
    results.append([file, normalized_counter])

# Create a DataFrame from the results
results_df = pd.DataFrame(results, columns=['File', 'Counter'])
results_df = results_df.sort_values(by='File')
# Save the results to a new CSV file
results_df.to_csv('comparison_results_ga.csv', index=False)

print("Comparison completed. Results saved to 'comparison_results.csv'.")

