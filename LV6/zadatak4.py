import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imageGrey= mpimg.imread(r"C:\Users\Luka\Desktop\example_grayscale.png")

X = imageGrey.reshape(-1, 1)

n_colors = 10
km = KMeans(n_clusters=n_colors, init='k-means++', n_init=10, random_state=0)
km.fit(X)

compressedX = km.cluster_centers_[km.labels_]
imageCompressed = compressedX.reshape(imageGrey.shape)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(imageGrey, cmap='gray')
ax[0].set_title('Originalna slika')
ax[1].imshow(imageCompressed, cmap='gray')
ax[1].set_title(f'Kvantizirana slika ({n_colors} boja)')
plt.show()