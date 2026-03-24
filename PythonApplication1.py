import pandas as pd

mtcars = pd.read_csv("mtcars.csv")

najveca_potrosnja = mtcars.sort_values(by=["mpg"]).head(5)
print("top 5 auta s najvecom potrosnjom", najveca_potrosnja[["car", "mpg"]])

najmanja_potrosnja = mtcars[mtcars.cyl == 8].sort_values(by=["cyl"]).head(3)
print("najmanja potrosnja tri automobila s 8 cilindra", najmanja_potrosnja[["car", "cyl"]])

srednja6_cyl = mtcars[mtcars.cyl == 6]["mpg"].mean()
print("srednja potrosnja automobila : ", srednja6_cyl, "mpg") 

srednja4_cyl = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)]["mpg"].mean()
print("srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs", srednja4_cyl, "mpg")

mjenjac_count = mtcars.groupby("am")["car"].count()
print("broj automobila po mjenjacu 0 = automatik , 1 = mjenjac", mjenjac_count)

auto_preko_100hp = len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)])
print ("broj automatika preko 100hp", auto_preko_100hp)

mtcars["masa_kg"] = mtcars.wt * 1000 * 0.453592
print("masa automobila u kg je",mtcars[["car", "masa_kg"]].head())



