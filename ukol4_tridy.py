from enum import auto


class Auta:
    def __init__(self, reg_znacka, typ_vozidla, pocet_km, stav = True): 
      self.reg_znacka = reg_znacka
      self.typ_vozidla = typ_vozidla
      self.pocet_km = pocet_km
      self.stav = stav
    def pujc_auto (self): 
      if self.stav == False:
         return f"Auto: {self.typ_vozidla} není k dispozici."
      else:
         self.stav = False
         return f"Auto: {self.typ_vozidla} je k dispozici. Potvrzuji půjčení auta."
    def get_info(self):
      return f"{self.reg_znacka}, {self.typ_vozidla}"



auto1 = Auta("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auta("1P3 4747", "Škoda Octavia", 41253,)

vyber_auto = (input("Jaké auto si přejete půjčit? Můžete si vybrat buď Škoda nebo Pegeot."))

if vyber_auto == "Pegeot":
   print (auto2.get_info())
   print (auto2.pujc_auto())
   print (auto2.pujc_auto())
elif vyber_auto == "Škoda":
    print (auto1.get_info())
    print (auto1.pujc_auto())
    print (auto1.pujc_auto())
else:
    print ("Takové auto nemáme.")

