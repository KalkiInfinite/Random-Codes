import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

disease_data = pd.read_csv('disease_data.csv')
dna_data = pd.read_csv('dna_data.csv')

data = pd.merge(disease_data, dna_data, on='patient_id')

X = data.drop(columns=['patient_id', 'disease_label'])
y = data['disease_label'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

new_dna_data = pd.read_csv('new_dna.csv')

new_data = new_dna_data.drop(columns=['patient_id'])
new_data = scaler.transform(new_data)

new_predictions = model.predict(new_data)

print("Predictions for new DNA files:", new_predictions)