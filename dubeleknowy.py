import unittest
from dubelek import Pomiar
from dubelek import wypluj_pom
class PomiaryTestCase(unittest.TestCase):
    def setUp(self):
        self.lista_pomiarow3 = [
            Pomiar('1', 4311, 'Lajka2'),
            Pomiar('2', 4411, 'Lajka2'),
            Pomiar('3', 3911, 'Lajka2'),
            Pomiar('4', 1211, 'Bajka'),
            Pomiar('5', 2311, 'Bajka'),
            Pomiar('6', 4511, 'Czajka'),
        ]
    def test_pomiary(self):
        result = wypluj_pom('Lajka2',self.lista_pomiarow3)
        expected = [4311,4411,3911]
        self.assertEqual(result,expected)
    def test_Bajka(self):
        result = wypluj_pom('Bajka', self.lista_pomiarow3)
        expected = [1211, 2311]
        self.assertEqual(result, expected)
    def test_exist(self):
        
# zadanie domowe
# dopiesz do pomiarów funkcje szukającej istnienia pomiarów dla wpisanego czujnika
# musi być test sprawdzający że zwraca True (AssertTrue)




