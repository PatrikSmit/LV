import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.0, 2.0, 3.0, 3.0, 1.0])
y = np.array([1.0, 2.0, 2.0, 1.0, 1.0])

plt.figure(figsize=(6,5))

plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2)
plt.axis([0,4,0,4])
plt.xlabel('x')
plt.ylabel('y')
plt.title('zadatak1')
plt.show()
