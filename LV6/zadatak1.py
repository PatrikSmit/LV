import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

n_samples = 500
flagc = 1
X = generate_data(n_samples, flagc)

n_clusters = 3
km = KMeans(n_clusters = n_clusters, init = 'random', n_init = 10, random_state=0)
y_km = km.fit_predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c = y_km, s = 50, cmap = 'viridis', label = 'Podatci po klasterima')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s = 250, marker='*', c = 'red', edgecolor='black', label = 'Centar klastera')

plt.title(f'K-means grupiranje podataka (flagc={flagc}, K={n_clusters})')
plt.xlabel('Prva ulazna velićina')
plt.ylabel('Druga ulazna velićina')
plt.legend()
plt.grid(True)
plt.show()
