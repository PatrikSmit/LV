import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

df = pd.read_csv(r'C:\Users\Luka\Desktop\occupancy_processed.csv', sep=',')

X = df[['S3_Temp', 'S5_CO2']]
Y = df['Room_Occupancy_Count']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train_scaled, Y_train)

Y_pred = clf.fit(X_train_scaled, Y_train).predict(X_test_scaled)

print("Matrica zabune: ")
print(confusion_matrix(Y_test, Y_pred))
print(f"\nTočnost: {accuracy_score(Y_test, Y_pred):.4f}")
print(f"\nPreciznost i odziv po klasama: ")
print(classification_report(Y_test, Y_pred))

plt.figure(figsize=(15, 10))
plot_tree(clf, feature_names=['S3_Temp', 'S5_CO2'], class_names=['Prazno', 'Zauzeto'], filled=True)
plt.show()