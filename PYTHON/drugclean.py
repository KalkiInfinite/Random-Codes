import pandas as pd
with open('filtered_file park.tsv', 'r') as f:
    lines = f.readlines()

cleaned_lines = [line for line in lines if len(line.split('\t')) == 14]
with open('cleaned_file.tsv', 'w') as f:
    f.writelines(cleaned_lines)

print("Non-tabular lines removed")
