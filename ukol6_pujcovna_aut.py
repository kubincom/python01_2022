
from dataclasses import replace
from enum import auto
from turtle import shapesize


nazev_souboru = "auta.txt"

with open(nazev_souboru, encoding='utf-8') as vstup:
  auta = vstup.readlines()


nahrazeni = [str(nahrazeni.replace(",",".")) for nahrazeni in auta]
rozdeleni = [spz.split() for spz in nahrazeni]
rozdeleni2 = [[spz[0], float(spz[1])] for spz in rozdeleni]
vysledek = sum(spz[1] for spz in rozdeleni2)*1000
print(f"Auta dohromady ujela {vysledek} km.")