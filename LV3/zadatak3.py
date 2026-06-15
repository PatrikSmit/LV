import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

url = 'https://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&tipPodatka=5&polutant=5&vrijemeOd=1.1.2017&vrijemeDo=31.12.2017'

airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)


df = pd.DataFrame(columns=['mjerenje', 'vrijeme'])
children = list(root)
i = 0

while True:
    try:
        obj = list(children[i])
    except:
        break

    try:
        vrijednost = float(obj[0].text)
        vrijeme = obj[2].text
        
        df.loc[i] = [vrijednost, vrijeme]
    except (IndexError, ValueError, TypeError):
        pass
    
    i = i + 1

df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)

df.plot(y='mjerenje', x='vrijeme', figsize=(10,5))
plt.title('Dnevne koncentracije PM10 u Osijeku (2017)')
plt.ylabel('Koncentracija ug/m3')
plt.show()

print("\nTri datuma s najvećom koncentracijom PM10 u 2017. godini:")

top_3 = df.sort_values(by='mjerenje', ascending=False).head(3)

for index, row in top_3.iterrows():
    print(f"Datum: {row['vrijeme'].strftime('%d.%m.%Y.')} - Koncentracija: {row['mjerenje']}")
