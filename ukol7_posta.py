
nazev_souboru = "posta.html"

with open(nazev_souboru, encoding='utf-8') as vstup:
  web = vstup.read()

import re
nahrazeni = web.replace("\n"," ")
print(re.sub(' +', ' ', 'nahrazeni'))

psc = re.compile(r"\d{3} \d{2} [A-Za-z]\w+ *[A-Za-z0-9]*\w+ *[A-Za-z0-9]*\w+ *[A-Za-z0-9]*\w+ *[A-Za-z0-9]*\w+")
print(psc.findall(nahrazeni))
vysledky = psc.findall(nahrazeni)
for vysledek in vysledky:
    print(vysledek)
