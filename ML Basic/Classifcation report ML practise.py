import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from tabulate import tabulate

df = pd.read_csv('sommin data1.csv')

X = df.drop('gender', axis=1)
y = df['gender']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=0)

# RandomForestClassifier
rf = RandomForestClassifier(random_state=0)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_val)
rf_acc = accuracy_score(y_val, rf_pred)
print('Accuracy of Random Forest is: {:.2f}%'.format(rf_acc*100))
rf_report = classification_report(y_val, rf_pred, output_dict=True)
df_report = pd.DataFrame(rf_report).transpose()
df_report = df_report.round(2)

print("\nClassification Report for Random Forest:")
print(tabulate(df_report, headers='keys', tablefmt='psql'))