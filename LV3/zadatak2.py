import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

mtcars = pd.read_csv(r"C:\Users\Luka\Desktop\mtcars.csv")

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

#a)
avg_mpg = mtcars.groupby('cyl')['mpg'].mean()
ax1.bar(avg_mpg.index.astype(str), avg_mpg.values, color='skyblue', edgecolor='black')
ax1.set_title('1. Prosječna potrošnja (MPG) po cilindrima')
ax1.set_xlabel('Broj cilindara')
ax1.set_ylabel('Milje po galonu (MPG)')

#b)
data_wt = [mtcars[mtcars['cyl'] == c]['wt'] for c in [4, 6, 8]]
ax2.boxplot(data_wt, tick_labels=['4', '6', '8'])
ax2.set_title('2. Distribucija težine po cilindrima')
ax2.set_xlabel('Broj cilindara')
ax2.set_ylabel('Težina (1000 lbs)')

plt.tight_layout()
plt.show()

fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 5))

#c)
data_am = [mtcars[mtcars['am'] == 0]['mpg'], mtcars[mtcars['am'] == 1]['mpg']]
ax3.boxplot(data_am, tick_labels=['Automatski (0)', 'Ručni (1)'])
ax3.set_title('3. Potrošnja: Automatski vs. Ručni mjenjač')
ax3.set_ylabel('Potrošnja (MPG)')

#d)
auto = mtcars[mtcars['am'] == 0]
manual = mtcars[mtcars['am'] == 1]
ax4.scatter(auto['hp'], auto['qsec'], color='red', label='Automatski', edgecolors='black')
ax4.scatter(manual['hp'], manual['qsec'], color='blue', label='Ručni', edgecolors='black')
ax4.set_title('4. Odnos ubrzanja i snage')
ax4.set_xlabel('Snaga (hp)')
ax4.set_ylabel('Ubrzanje (qsec)')
ax4.legend()

plt.tight_layout()
plt.show()
