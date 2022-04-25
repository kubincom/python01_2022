
nazev_souboru = "posta.html"

with open(nazev_souboru, encoding='utf-8') as vstup:
  web = vstup.read()

import re
nahrazeni = web.replace("\n"," ")
print(re.sub(' +', ' ', 'nahrazeni'))

psc = re.compile(r"\d{3} \d{2} [A-Z]\w+ [A-Z|0-9|]")
print(psc.findall(nahrazeni))
vysledky = psc.findall(nahrazeni)
for vysledek in vysledky:
    print(vysledek)