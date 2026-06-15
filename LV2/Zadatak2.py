import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open(r"C:\Users\student\desktop\Stark_LV2\mtcars.csv", "rb"), usecols = (1, 2, 3, 4, 5, 6), delimiter = ",", skiprows = 1)

mpg = data[ : , 0]
cyl = data[ : , 1]
hp = data[ : , 3]
wt = data[ : , 5]

plt.figure(figsize=(10, 10))

plt.scatter(mpg, hp, s = wt * 10, c = "blue")

#d) i e) dio zadatka

print("Svi automobili: ")
print(f"Minimalni mpg: {np.min(mpg):.2f}")
print(f"Maksimalni mpg: {np.max(mpg):.2f}")
print(f"srednja vrijednost mpg: {np.mean(mpg):.2f}")

mpgSestCilindara = mpg[cyl == 6]

print("Automobili sa 6 cilindara: ")
print(f"Minimalni mpg: {np.min(mpgSestCilindara):.2f}")
print(f"Maksimalni mpg: {np.max(mpgSestCilindara):.2f}")
print(f"Srednja vrijednost: {np.mean(mpgSestCilindara):.2f}")

#Nastavak prvog dijela zadatka

plt.title("Ovisnost potrosnje o konjskim snagama")
plt.xlabel("Konjska snaga(hp)")
plt.ylabel("Potrosnja(Miles per gallon)")
plt.grid(True)
plt.show()

