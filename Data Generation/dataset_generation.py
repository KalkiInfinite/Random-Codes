import pandas as pd
import numpy as np
import os

beta = {
    'Alzheimer\'s': [-3.0, 0.1],
    'Breast Cancer': [-4.0, 0.1],
    'Coronary Artery Disease': [-4.0, 0.15],
    'Parkinson\'s Disease': [-4.5, 0.1]
}

threshold = {
    'Alzheimer\'s Disease': 27.45448457628697,
    'Asthma': 68.86847585458283,
    'Breast Cancer': 31.555622424105263,
    'Coronary Artery Disease': 28.362071598015476, 
    'Diabetes Mellitus Type 1': 21.472475744600086, 
    'Diabetes Mellitus Type 2': 55.695030213387476,
    'Ischemic Stroke': 10.884100038869343,
    'Lung Carcinoma': 18.294513980950068,
    'Parkinson\'s Disease': 10.573534983890493, 
    'Pulmonary Fibrosis': 9.989312428347842
}

disease_association = pd.read_csv(r'C:\Users\piyus\Downloads\Data Generation\Data Generation\DiseaseAssociation.csv')
folder_path = r'C:\Users\piyus\Downloads\Data Generation\Data Generation\User Data'

for root, dirs, files in os.walk(folder_path):
    for file in files:

        file_path = os.path.join(root, file)
        dna_data = pd.read_csv(file_path)

        features = pd.merge(dna_data, disease_association, on='rsid')

        features['risk_allele_frequency'] = ((features['allele1'] == features['risk_allele']).astype(float) + 
                                                (features['allele2'] == features['risk_allele']).astype(float))

        refined_features = features.dropna(subset=['odds_ratio']).copy()

        refined_features['mrs'] = features['risk_allele_frequency'] * np.log(features['odds_ratio'])

        prs_values = refined_features.groupby('disease_name')['mrs'].sum().to_dict()

        final_features = pd.DataFrame()
        final_features['key'] = features['rsid']+ "_" + features['disease_name']

        final_features['risk_allele_frequency'] = features['risk_allele_frequency'] / 2

        for disease in prs_values:
            if(prs_values[disease] >= threshold[disease]):
                final_features.loc[len(final_features.index)] = [disease, 1]
            else:
                final_features.loc[len(final_features.index)] = [disease, 0]

        final_features = final_features.transpose()
        final_features.columns = final_features.iloc[0]
        final_features = final_features.drop(final_features.index[0]).reset_index(drop=True)

        dataset = pd.read_csv(r'C:\Users\piyus\Downloads\Data Generation\Data Generation\Dataset.csv')
        dataset = dataset[final_features.columns]
     
        new_dataset = pd.concat([dataset, final_features], ignore_index=True)
        new_dataset.to_csv(r'C:\Users\piyus\Downloads\Data Generation\Data Generation\Dataset.csv', index=False)