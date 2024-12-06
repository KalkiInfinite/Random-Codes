import pandas as pd

def process_files(file_paths):
    dfs = [pd.read_table(file) for file in file_paths]

    common_rsids = set(dfs[0]['rsid'])
    for df in dfs[1:]:
        common_rsids = common_rsids.intersection(set(df['rsid']))

    new_dfs = [df[df['rsid'].isin(common_rsids)] for df in dfs]

    for i, new_df in enumerate(new_dfs):
        new_df.to_csv(f'new_user{i + 1}.csv', index=False)

    print("Files processed and saved successfully.")

file_paths = [
    r'12730ancestry.txt', r'12734ancestry.txt', r'12728ancestry.txt', r'12669ancestry.txt',
    r'12680ancestry.txt', r'12683ancestry.txt', r'12687ancestry.txt', r'12723ancestry.txt',
    r'12725ancestry.txt', r'12729ancestry.txt', r'12734ancestry.txt', r'12736ancestry.txt',
    r'12730ancestry.txt', r'12731ancestry.txt', r'12742ancestry.txt'
]

if len(file_paths) == 15:
    process_files(file_paths)
else:
    print(f"Error: You must provide exactly 15 file paths, but {len(file_paths)} were given.")