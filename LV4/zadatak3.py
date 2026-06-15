import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x_reshaped = x[:, np.newaxis]
y_reshaped = y_measured[:, np.newaxis]

degrees = [2, 6, 15]
MSEtrain = []
MSEtest = []

plt.figure(figsize=(12, 8))
plt.plot(x, y_true, 'k--', label='Pozadinska funkcija (f)', linewidth=2)
plt.scatter(x, y_measured, color='gray', alpha=0.5, label='Izmjereni podaci')

for d in degrees:
    poly = PolynomialFeatures(degree=d)
    x_poly = poly.fit_transform(x_reshaped)
    
    np.random.seed(12)
    indeksi = np.random.permutation(len(x_poly))
    split = int(np.floor(0.7 * len(x_poly)))
    indeksi_train = indeksi[:split]
    indeksi_test = indeksi[split:]
    
    xtrain, ytrain = x_poly[indeksi_train], y_reshaped[indeksi_train]
    xtest, ytest = x_poly[indeksi_test], y_reshaped[indeksi_test]
    
    model = lm.LinearRegression()
    model.fit(xtrain, ytrain)
    
    ytrain_p = model.predict(xtrain)
    ytest_p = model.predict(xtest)
    
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    MSEtest.append(mean_squared_error(ytest, ytest_p))
    
    y_plot = model.predict(poly.transform(x_reshaped))
    plt.plot(x, y_plot, label=f'Model stupnja {d}')

print(f"Stupnjevi: {degrees}")
print(f"MSE Train: {MSEtrain}")
print(f"MSE Test:  {MSEtest}")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Usporedba modela različitih stupnjeva s pozadinskom funkcijom')
plt.legend()
plt.show()
