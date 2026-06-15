import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

n_samples = 500
flagc = 1
X = generate_data(n_samples, flagc)

vrijednostiKriterijskeFunkcije = []
K_raspon = range(1, 21)

for k in K_raspon:
    km = KMeans(n_clusters=k, init='random', n_init=10, random_state=0)
    km.fit(X)
    vrijednostiKriterijskeFunkcije.append(km.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(K_raspon, vrijednostiKriterijskeFunkcije, marker='o', linestyle = '--')
plt.xlabel('Broj klastera(K)')
plt.ylabel('Vrijednost kriterijske funkcije (Inercija)')
plt.title('Lakat metoda za određivanje optimalnog K')
plt.xticks(K_raspon)
plt.grid(True)
plt.show()