import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error

df = pd.read_csv(r'C:\Users\Luka\Desktop\cars_processed.csv')

categoricals = ['fuel', 'seller_type', 'transmission', 'owner']
df_final = pd.get_dummies(df, columns=categoricals, drop_first=True)

X = df_final.drop(columns=['name', 'selling_price'])
Y = df_final['selling_price']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, Y_train)

Y_train_pred = model.predict(X_train_scaled)
Y_test_pred = model.predict(X_test_scaled)

print("Rezultati novog testnog skupa: ")
print(f"Novi mean absolute error: {mean_absolute_error(Y_test, Y_test_pred):.2f}")
print(f"Novi mean squared error: {mean_squared_error(Y_test, Y_test_pred):.2f}")
print(f"Novi R2 score: {r2_score(Y_test, Y_test_pred)}")
print(f"Novi max error: {max_error(Y_test, Y_test_pred)}")
