import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

df = pd.read_csv(r'C:\Users\Luka\Desktop\occupancy_processed.csv', sep=',')
X = df[['S3_Temp', 'S5_CO2']]
Y = df['Room_Occupancy_Count']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logReg = LogisticRegression()
logReg.fit(X_train_scaled, Y_train)

Y_pred = logReg.predict(X_test_scaled)

print("Matrica zabune: ")
print(confusion_matrix(Y_test, Y_pred))
print(f"\Točnost: {accuracy_score(Y_test, Y_pred):.4f}")
print("\nPreciznost i odziv po klasama: ")
print(classification_report(Y_test, Y_pred))

