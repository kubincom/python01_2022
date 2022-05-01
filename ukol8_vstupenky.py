from datetime import datetime, timedelta
from ssl import VERIFY_CRL_CHECK_CHAIN
from tokenize import Floatnumber


datum_akce =  str(input("Zadejte datum, kdy chcete jít do kina (s mezerami mezi datem, měsícem a rokem): "))
datum_akce = datetime.strptime(datum_akce,"%d. %m. %Y")
if datum_akce  >= datetime(2022, 7, 1) and datum_akce <= datetime(2022, 8, 31):
  pocet_osob = int(input("Zadejte počet osob:"))
  datum_zmeny_ceny = datetime(2022, 8, 11)
  if datum_akce <= datum_zmeny_ceny:
      cena = pocet_osob*250
  else:
      cena = pocet_osob*180
  print(f"Vstupenky stojí {cena}.")
else:
  print ("V tento měsíc se nehraje.")

