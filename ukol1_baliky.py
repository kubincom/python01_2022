baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

print ("zjistíme stav balíku")
balik = str(input("jaký je kód balíku?"))

if balik in baliky.keys():
      if baliky[balik] == False: 
        print("Balík zatím nebyl předán kurýrovi.")
      if baliky[balik] == True:
        print("Balík byl předán kurýrovi.")
else:
    print ("Balík nenalezen.")
