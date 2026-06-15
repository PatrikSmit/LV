import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image = mpimg.imread(r"C:\Users\Luka\Desktop\example.png")

w, h, d = image.shape
X = image.reshape((-1, 3))

n_colors = 10
km = KMeans(n_clusters=n_colors, init='k-means++', n_init=10, random_state=0)
km.fit(X)

new_colors = km.cluster_centers_[km.labels_]

image_kvant = new_colors.reshape((w, h, d))

fig, ax = plt.subplots(1, 2, figsize=(15, 7))
ax[0].imshow(image)
ax[0].set_title('Originalna slika:')
ax[0].axis('off')

ax[1].imshow(image_kvant)
ax[1].set_title(f'Kvantizirana slika sa {n_colors} boja')
ax[1].axis('off')

plt.show()



