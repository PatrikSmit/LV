import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay

df = pd.read_csv('occupancy_processed.csv', sep=',')

print(df.columns)
print(df.columns.to_list())

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count' 
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
Y = df[target_name].to_numpy()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, Y_train)

Y_pred = knn.predict(X_test_scaled)

cm = confusion_matrix(Y_test, Y_pred)
print("Matrica zabune:\n", cm)

accuracy = accuracy_score(Y_test, Y_pred)
print(f"Točnost: {accuracy:.4f}")

print("\nKlasifikacije:")
print(classification_report(Y_test, Y_pred, target_names=class_names))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Matrica zabune")
plt.show()