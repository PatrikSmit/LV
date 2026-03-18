def total_euro(sati, cijena):
    return sati * cijena

sati = float(input("Radni sati: "))
cijena = float(input("eura/h: "))

ukupno = total_euro(sati, cijena)

print("Ukupno:", ukupno, "eura")
