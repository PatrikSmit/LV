import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error

df = pd.read_csv(r'C:\Users\Luka\Desktop\cars_processed.csv')

X = df.drop(columns=['name', 'selling_price', 'fuel', 'seller_type', 'transmission', 'owner'])
Y = df['selling_price']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, Y_train)

Y_train_pred = model.predict(X_train_scaled)
Y_test_pred = model.predict(X_test_scaled)

print("Rezultati testnog skupa: ")
print(f"Mean absolute error: {mean_absolute_error(Y_test, Y_test_pred):.2f}")
print(f"Mean squared error: {mean_squared_error(Y_test, Y_test_pred):.2f}")
print(f"R2 score: {r2_score(Y_test, Y_test_pred)}")
print(f"Max error: {max_error(Y_test, Y_test_pred)}")