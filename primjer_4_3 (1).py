import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error



# Učitavanje očišćenih podataka
df = pd.read_csv('cars_processed.csv')
scaler = MinMaxScaler()
sScaler = StandardScaler()
model = LinearRegression()
#print(df.info())
# # Automobil s najvećom i najmanjom cijenom

# max_price_row = df.loc[df['selling_price'].idxmax()]
# min_price_row = df.loc[df['selling_price'].idxmin()]
# # Broj automobila proizvedenih 2012. godine

# cars_2012 = df[df['year'] == 2012]
# num_cars_2012 = cars_2012.shape[0]
# print(f"Broj automobila proizvedenih 2012. godine: {num_cars_2012}")

# # Automobil s najviše i najmanje prijeđenih kilometara
# max_km_row = df.loc[df['km_driven'].idxmax()]
# min_km_row = df.loc[df['km_driven'].idxmin()]

# # Najčešći broj sjedala u automobilima
# seat_counts = df['seats'].value_counts()
# most_common_seats = seat_counts.idxmax()
# print(f"Najčešći broj sjedala: {most_common_seats}")


# print("Automobil s najviše prijeđenih kilometara:")
# print(max_km_row)

# print("\nAutomobil s najmanje prijeđenih kilometara:")
# print(min_km_row)

# print("Automobil s najvećom cijenom:")
# print(max_price_row)

# print("\nAutomobil s najmanjom cijenom:")
# print(min_price_row)
# # Prosječna kilometraža za dizel i benzinske automobile
# average_km_diesel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
# average_km_petrol = df[df['fuel'] == 'Petrol']['km_driven'].mean()

# print(f"Prosječna kilometraža za dizel automobile: {average_km_diesel} km")
# print(f"Prosječna kilometraža za benzinske automobile: {average_km_petrol} km")

# Različiti prikazi
df = df.drop(['name'], axis=1)
#df = df.drop(['fuel'], axis=1)
#df = df.drop(['seller_type'], axis=1)
#df = df.drop(['transmission'], axis=1)
#df = df.drop(['owner'], axis=1)

# one-hot encoding za sve kategorijske varijable
df_encoded = pd.get_dummies(df, drop_first=True)


# Razdvajanje skupa podataka na ulazne značajke (X) i ciljnu varijablu (y)
X = df_encoded.drop('selling_price', axis=1)  # Ulazne značajke (sve osim 'selling_price')
y = df_encoded['selling_price']  # Ciljna varijabla (cijena)

# Podjela skupa podataka na trening (80%) i test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Provjera dimenzija podjela
print(X_train.shape, X_test.shape)
# Skaliranje podataka
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled, y_train)

# Parametri modela (koeficijenti i intercept)
print(f'Intercept: {model.intercept_}')
print(f'Koeficijenti: {model.coef_}')

# Predikcija na trening i test skupu
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Evaluacija modela na trening skupu
mae_train = mean_absolute_error(y_train, y_train_pred)
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)
max_err_train = max_error(y_train, y_train_pred)

# Evaluacija modela na test skupu
mae_test = mean_absolute_error(y_test, y_test_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)
max_err_test = max_error(y_test, y_test_pred)

# Ispis rezultata
print("Evaluacija modela na trening skupu:")
print(f'MAE (trening): {mae_train}')
print(f'MSE (trening): {mse_train}')
print(f'R2 (trening): {r2_train}')
print(f'Max Error (trening): {max_err_train}')

print("\nEvaluacija modela na test skupu:")
print(f'MAE (test): {mae_test}')
print(f'MSE (test): {mse_test}')
print(f'R2 (test): {r2_test}')
print(f'Max Error (test): {max_err_test}')








# sns.pairplot(df, hue='fuel')

# sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
# df = df.drop(['name', 'mileage'], axis=1)

# # Razdvajanje kategorijskih i numeričkih kolona
# obj_cols = df.select_dtypes(include=['object']).columns.values.tolist()
# num_cols = df.select_dtypes(include=[np.number]).columns.values.tolist()

# # Prikaz broja pojavljivanja kategorijskih varijabli
# fig = plt.figure(figsize=[15, 8])
# for col in range(len(obj_cols)):
#     plt.subplot(2, 2, col + 1)
#     sns.countplot(x=obj_cols[col], data=df)

# # Boxplot za 'selling_price' po gorivu
# df.boxplot(by='fuel', column=['selling_price'], grid=False)

# # Histogram za 'selling_price'
# df.hist(['selling_price'], grid=False)

# # Izračun korelacije samo za numeričke kolone
# tabcorr = df[num_cols].corr()  # Ovdje uzimamo samo numeričke kolone za korelaciju

# # Heatmap korelacije
# sns.heatmap(tabcorr, annot=True, linewidths=2, cmap='coolwarm')

# plt.show()