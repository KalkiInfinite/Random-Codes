import pandas as pd
import random

size = 500

file_path = r'C:\Users\piyus\Downloads\Data Generation\Data Generation\user1.csv'
df = pd.read_csv(file_path)

alleles = ['A', 'C', 'T', 'G']

def randomize_alleles(df):
    df['allele1'] = df['allele1'].apply(lambda x: random.choice(alleles))
    df['allele2'] = df['allele2'].apply(lambda x: random.choice(alleles))
    return df

folder_path = r'C:\Users\piyus\Downloads\Data Generation\Data Generation\User Data'
for i in range(1, size+1):
    new_df = randomize_alleles(df.copy()) 
    
    output_file_path = f'\\user{i}.csv'
    new_df.to_csv(folder_path + output_file_path, index=False)