# Stwórz klase pomiar która będzie zawierać numer pomiaru , temp w  C i nazwe
# (czujnika).Stwóz funkcję która wyświetli wszystkie pomiary dla danego czujnika.
# *Argumentem funkcji będzie nazwa czujnika i lista pomiarów.
import unittest

class Pomiar():
    def __init__(self,num_pom,temp_C,naz_czuj):
        self.num_pom = num_pom
        self.temp_C = temp_C
        self.naz_czuj = naz_czuj

lista_pomiarow = [
    Pomiar('1',43,'Lajka'),
    Pomiar('2',44,'Lajka'),
    Pomiar('3',39,'Lajka'),
    Pomiar('4',12,'Bajka'),
    Pomiar('5',23,'Bajka'),
    Pomiar('6',45,'Czajka'),

]

lista_pomiarow2 = [
    Pomiar('1',100,'Lajka'),
    Pomiar('2',444,'Lajka'),
    Pomiar('3',394,'Lajka'),
    Pomiar('4',125,'Bajka'),
    Pomiar('5',235,'Bajka'),
    Pomiar('6',455,'Czajka'),

]


def wypluj_pom(naz_czuj,pomiary):
    lista_wynik = []
    for pomiar in pomiary:
        if naz_czuj == pomiar.naz_czuj:
            lista_wynik += [pomiar.temp_C]

        else:
            pass
    return lista_wynik

class PomiaryTestCase(unittest.TestCase):
    def test_pomiary(self):
        lista_pomiarow3 = [
            Pomiar('1', 4311, 'Lajka2'),
            Pomiar('2', 4411, 'Lajka2'),
            Pomiar('3', 3911, 'Lajka2'),
            Pomiar('4', 1211, 'Bajka'),
            Pomiar('5', 2311, 'Bajka'),
            Pomiar('6', 4511, 'Czajka'),
        ]
        result = wypluj_pom('Lajka2',lista_pomiarow3)
        expected = [4311,4411,3911]
        self.assertEqual(result,expected)






