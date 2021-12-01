# zadanie domowe
# dopiesz do pomiarów funkcje szukającej istnienia pomiarów dla wpisanego czujnika
# musi być test sprawdzający że zwraca True (AssertTrue)
import unittest


class Czujnik():
    def __init__(self,nazwa,num_pom,wynik):
        self.nazwa = nazwa
        self.num_pom = num_pom
        self.wynik = wynik

lista_pomiarow = [
    Czujnik('Ptak',1,134),
    Czujnik('Ptak',2,234),
    Czujnik('Ptak',3,156),
    Czujnik('Srak',1,342),
    Czujnik('Srak',2,291),
    Czujnik('Fiat',1,191),
]

def czy_jest(nazwa,lista):
    for czujnik in lista:
        if nazwa == czujnik.nazwa:
            return True

    return False

czy_jest('Fiat',lista_pomiarow)
czy_jest('Srak',lista_pomiarow)
czy_jest('Huj_w_dupie',lista_pomiarow)
czy_jest('Srak',[Czujnik('Srak',1,199)])

