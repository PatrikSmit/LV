import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(r"C:\Users\Luka\Desktop\LV2\tiger.png")
img = img[:,:,0].copy()

#a)
if img.max() <= 1.0:
    imgA = np.clip(img + 0.5, 0, 1)
else:
    imgA = np.clip(img + 125, 0, 255) 

#b)
imgB = np.rot90(img, k= -1)

#c)
imgC = np.fliplr(img)

#d)
imgD = img[::10, ::10]

#e)
imgE = np.zeros_like(img)
visina, sirina = img.shape

pocetakCet = sirina // 4
krajCet = sirina // 2

imgE[:, pocetakCet:krajCet] = img[:, pocetakCet:krajCet]

#prikaz rezultata
plt.figure(figsize=(12, 8))

naslovi = ["Original", "a) Svijetlija slika", "b) Rotirano 90 stupnjva", "c) Zrcaljeno", "d) Smanjena rezolucija 10 puta", "Druga cetvrtina jedina vidljiva"]
slike = [img, imgA, imgB, imgC, imgD, imgE]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    limit = 1.0 if img.max() <= 1.0 else 255
    plt.imshow(slike[i], cmap = 'gray', vmin = 0, vmax = limit)
    plt.title(naslovi[i])
    plt.axis('off')

plt.tight_layout()
plt.show()


