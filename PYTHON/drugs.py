import pandas as pd

input_file_path = 'all-data park.tsv'
filtered_file_path = 'filtered_file.tsv'
cleaned_file_path = 'cleaned_file.tsv'

df = pd.read_csv(input_file_path, sep='\t')
filtered_df = df[df['Variant'].str.startswith('rs')]

filtered_df.to_csv(filtered_file_path, sep='\t', index=False)
print("Rows filtered")

with open(filtered_file_path, 'r') as f:
    lines = f.readlines()

cleaned_lines = [line for line in lines if len(line.split('\t')) == 14]

with open(cleaned_file_path, 'w') as f:
    f.writelines(cleaned_lines)

print("Non-tabular lines removed")

