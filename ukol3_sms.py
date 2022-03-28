def sms_rozesilka(cislo: int,):
    if len(cislo) == 9:
      return True
    elif len(cislo) == 13:
      if "+420" in cislo:
        return True
      else: 
        return False
    else:
      return False

def sms_rozesilka_text():
     cena = round(((len(zprava))//180+1)*3)  
     print (f"Vaše sms na tel. číslo {cislo} byla odeslana za {cena} Kč.")
   

cislo = (input("Zadej číslo: "))
cislo = cislo.replace(" ", "")
zprava= input("jakou zprávu chcete poslat? ")

if sms_rozesilka(cislo) == False:
      print("špatné telefonní číslo")
else:
  sms_rozesilka_text()

