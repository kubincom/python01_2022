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

cislo = (input("Zadej číslo: "))
cislo = cislo.replace(" ", "")
if sms_rozesilka(cislo) == False:
      print("špatné telefonní číslo")
else:
  zprava = (input("jakou zprávu chcete poslat? "))
  cena = round(((len(zprava))//180+1)*3)
  print (f"Cena sms je {cena} Kč.")

