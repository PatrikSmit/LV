try:
    ocjena= float(input("Napisi ocjenu izmedu 0.0 i 1.0:"))
    if ocjena < 0.0 or ocjena > 1.0:
        print("Greska: broj mora biti u intervalu od 0.0 do 1.0")
    elif ocjena>=0.9:
        print("A")
    elif ocjena>=0.8:
        print("B")
    elif ocjena>=0.7:
        print("C")
    elif ocjena>=0.6:
        print("D")
    elif ocjena <0.6:
        print("F")
except:
    print("Greska: Niste unjeli broj")