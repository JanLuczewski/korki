import unittest
from zadanie_domowe_29_11 import Czujnik
from zadanie_domowe_29_11 import czy_jest
class CzujnikTestCase(unittest.TestCase):
    def setUp(self):
        self.lista_pomiarow_do_testu = [
            Czujnik('Ptak', 1, 134),
            Czujnik('Ptak', 2, 234),
            Czujnik('Ptak', 3, 156),
            Czujnik('Srak', 1, 342),
            Czujnik('Srak', 2, 291),
            Czujnik('Fiat', 1, 191),
        ]
    def test_czujnik(self):
        result = czy_jest('Srak',self.lista_pomiarow_do_testu)
        self.assertTrue(result)
    def test_czujnik__negative(self):
        result = czy_jest('Gdak_nonexist',self.lista_pomiarow_do_testu)
        self.assertFalse(result)
