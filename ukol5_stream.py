class Polozka:
 def __init__ (self, nazev, zanr):
   self.nazev = nazev
   self.zanr = zanr
 def get_info (self):
    return f"{self.nazev}, {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):  
        super().__init__(nazev, zanr)
        self.delka = delka
  def get_info(self):
    return (super().get_info()+ f",{self.delka}")

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, epizoda):  
        super().__init__(nazev, zanr)
        self.pocet_epizod =pocet_epizod
        self.epizoda = epizoda
  def get_info(self):
    return (super().get_info()+ f",{self.pocet_epizod}, {self.epizoda}")

film = Polozka("Kmotr", "thriller")
film2 = Film("Kmotr", "thriller",120)
serial = Serial ("Červený trpaslík", "komedie",40, 15)


print(film.get_info())
print(film2.get_info())
print(serial.get_info())