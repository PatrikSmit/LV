import pandas as pd

data = pd.read_csv("mtcars.csv")

#a)
najveca_potrosnja = data.sort_values(by="mpg").head(5)
print("Pet auta s najvećom potrošnjom:\n", najveca_potrosnja[["car", "mpg"]])

#b)
najmanja_potrosnja_osam_cilindara = data[data["cyl"] == 8].sort_values(by="mpg", ascending=False).head(3)
print(f"Auti s 8 cilindara s najmanjom potrošnjom:\n {najmanja_potrosnja_osam_cilindara}")

#c)
srednja_potrošnja_sest_cilindara = data[data["cyl"] == 6]["mpg"].mean()
print(f"Srednja potrošnja auta sa šest cilindara: {srednja_potrošnja_sest_cilindara}")

#d)
srednja_potrosnja_cetiri_cilindra = data[(data["cyl"] == 4) & (2 <= data["wt"]) & (data["wt"] <= 2.2)]["mpg"].mean()
print(f"Srednja potrošnja auta s četiri cilindra i mase između 2000 i 2200 libri: {srednja_potrosnja_cetiri_cilindra}") 

#e)
rucni_mijenjac = data[data["am"] == 1].shape[0]
automatski_mijenjac = data[data["am"] == 0].shape[0]
print(f"Rucni mijenjač: {rucni_mijenjac}, automatski mijenjač: {automatski_mijenjac}")

#f)
automatski_preko_100_hp = data[(data["am"] == 0) & (data["hp"] > 100)].shape[0]
print(f"Auti s automatskim mijenjačem i preko 100 konjskih snaga: {automatski_preko_100_hp}")

#g)
data["masa_u_kg"] = (data["wt"] * 0.45359) * 1000
print(f"Masa svih automobila u kilogramima je:\n {data[["car", "masa_u_kg"]]}")



