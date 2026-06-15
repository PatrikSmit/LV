import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from funkcija_6_1 import generate_data

n_samples = 500
flagc = 1
X = generate_data(n_samples, flagc)

method = 'complete'
clusters = linkage(X, method=method)

plt.figure(figsize=(10, 7))
plt.title(f'Dendrogram: {method}')
plt.xlabel('Veličina klastera')
plt.ylabel('Euklidska ualjenost')
dendrogram(clusters, truncate_mode='lastp', p = 20, leaf_rotation=90., leaf_font_size=10., show_contracted=True)
plt.show()
