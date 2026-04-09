import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Generiranje stvarne funkcije i podataka s šumom
def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1 * varNoise * np.random.normal(0, 1, len(y))
    return y_noisy

# Generiranje podataka
x = np.linspace(1, 10, 50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# Podjela na trening i test skup
np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:]

xtrain = x[indeksi_train]
ytrain = y_measured[indeksi_train]

xtest = x[indeksi_test]
ytest = y_measured[indeksi_test]

# Polinomski stupnjevi koje ćemo testirati
degrees = [2, 6, 15]

MSEtrain = []
MSEtest = []

# Kretanje kroz različite stupnjeve polinoma
for degree in degrees:
    # Transformacija podataka u polinomske značajke
    poly = PolynomialFeatures(degree=degree)
    xtrain_poly = poly.fit_transform(xtrain)
    xtest_poly = poly.transform(xtest)
    
    # Trening modela
    linearModel = lm.LinearRegression()
    linearModel.fit(xtrain_poly, ytrain)
    
    # Predikcije i MSE
    ytrain_pred = linearModel.predict(xtrain_poly)
    ytest_pred = linearModel.predict(xtest_poly)
    
    MSEtrain.append(mean_squared_error(ytrain, ytrain_pred))
    MSEtest.append(mean_squared_error(ytest, ytest_pred))

# Prikaz rezultata MSE za svaki stupanj
print("MSE za trening skup (degree = 2, 6, 15):", MSEtrain)
print("MSE za test skup (degree = 2, 6, 15):", MSEtest)

# Grafički prikaz modela za tri stupnja polinoma
x_range = np.linspace(1, 10, 200)[:, np.newaxis]
plt.figure(figsize=(10, 6))

for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    xtrain_poly = poly.fit_transform(xtrain)  # Transformiraj trening podatke
    xtest_poly = poly.transform(xtest)  # Transformiraj testne podatke
    
    # Definiraj model i treniraj ga
    linearModel = lm.LinearRegression()
    linearModel.fit(xtrain_poly, ytrain)
    
    # Primijeniti istu transformaciju na x_range za predikciju
    x_range_poly = poly.transform(x_range)  # Koristi transformaciju na novim podacima
    
    # Predikcija
    y_range_pred = linearModel.predict(x_range_poly)
    
    # Crtanje predikcija
    plt.plot(x_range, y_range_pred, label=f"Model degree={degree}")
    
plt.plot(x, y_true, label="True function", color='black', linewidth=2)
#plt.scatter(xtrain, ytrain, color='blue', label="Training data", zorder=5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Models for Different Polynomial Degrees')
plt.show()
# Simulacija utjecaja broja uzoraka na rezultate
sample_sizes = [20, 50, 100]
for sample_size in sample_sizes:
    x = np.linspace(1, 10, sample_size)
    y_true = non_func(x)
    y_measured = add_noise(y_true)
    
    x = x[:, np.newaxis]
    y_measured = y_measured[:, np.newaxis]

    np.random.seed(12)
    indeksi = np.random.permutation(len(x))
    indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
    indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:]

    xtrain = x[indeksi_train]
    ytrain = y_measured[indeksi_train]

    xtest = x[indeksi_test]
    ytest = y_measured[indeksi_test]

    MSEtrain = []
    MSEtest = []

    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        xtrain_poly = poly.fit_transform(xtrain)
        xtest_poly = poly.transform(xtest)
        
        linearModel = lm.LinearRegression()
        linearModel.fit(xtrain_poly, ytrain)
        
        ytrain_pred = linearModel.predict(xtrain_poly)
        ytest_pred = linearModel.predict(xtest_poly)
        
        MSEtrain.append(mean_squared_error(ytrain, ytrain_pred))
        MSEtest.append(mean_squared_error(ytest, ytest_pred))
    
    print(f"\nSample size: {sample_size}")
    print("MSE for training set:", MSEtrain)
    print("MSE for test set:", MSEtest)