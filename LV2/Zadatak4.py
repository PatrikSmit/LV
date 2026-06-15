import numpy as np
import matplotlib.pyplot as plt

def napraviSahovnicu(kvadratVelicina, kvadratVisina,kvadratSirina):
    crnoPolje = np.zeros((kvadratVelicina, kvadratVelicina), dtype=np.uint8)
    bijeloPolje = np.ones((kvadratVelicina, kvadratVelicina), dtype=np.uint8) * 255

    red1 = [crnoPolje if i % 2 == 0 else bijeloPolje for i in range(kvadratSirina)]
    red1_spojen = np.hstack(red1)

    red2 = [bijeloPolje if i % 2 == 0 else crnoPolje for i in range(kvadratSirina)]
    red2_spojen = np.hstack(red2)

    sahovnicaList = []
    for i in range(kvadratVisina):
        if i % 2 == 0:
            sahovnicaList.append(red1_spojen)
        else:
            sahovnicaList.append(red2_spojen)

    sahovnicaImg = np.vstack(sahovnicaList)
    
    return sahovnicaImg

mojePolje = napraviSahovnicu(kvadratVelicina=50,kvadratVisina= 4,kvadratSirina= 5)

plt.figure()
plt.imshow(mojePolje, cmap = 'gray', vmin = 0, vmax = 255)
plt.tight_layout()
plt.show()



