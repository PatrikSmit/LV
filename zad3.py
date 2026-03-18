brojevi = []

    
    
try:
    while True:
        unos= input("Unesite brojeve ili Done za zavrsetak")
        if unos == "Done":
            break
        
        broj=float(unos)
        brojevi.append(broj)
except:
    print("Pogresan unos, unesi broj")

if len(brojevi)== 0:
    print("nema unesenih brojeva")
else:
    print("Srednja vrijednost brojeva je: ",sum(brojevi)/len(brojevi))
    print("Minimalna vrijednost: ",min(brojevi))
    print("Maksimalna vrijednost",max(brojevi))
    print("Broj ispisanih brojeva:", len(brojevi))
brojevi.sort()
print("Sortirani brojevi", brojevi)

