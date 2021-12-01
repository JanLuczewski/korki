# Stwórz funkcje która będzie liczyła pole prostokątu.
import unittest
from funkcja_do_testu import pole_prostokata
from funkcja_do_testu import czy_kwadrat

class PoleTestCase(unittest.TestCase):
    def test_kwadrat_pozytyw(self):
        result = pole_prostokata(3,3)
        expected = 9
        self.assertEqual(result,expected)
    def test_prostokat_pozytyw(self):
        result = pole_prostokata(2,3)
        expected = 6
        self.assertEqual(result,expected)
    def test_czy_liczbowy(self):
        result = pole_prostokata('2',3)
        expected = 'bez stringow prosze'
        self.assertEqual(expected,result)
class KwadratTestCase(unittest.TestCase):
    def test_czy_to_kwadrat_positive(self):
        result = czy_kwadrat(2,2)
        expected = "to jest kwadrat"
        self.assertEqual(result,expected)
    def test_czy_to_kwadrat_negative(self):
        result = czy_kwadrat(4,3)
        expected = 'to nie jest kwadrat ty gamoniu'
        self.assertEqual(result,expected)
    def test_czy_to_inty_positive(self):
        result = czy_kwadrat(4,'kupa')
        expected = 'podane wartosci NIE sa liczbowe'
        self.assertEqual(result,expected)

# napisz funkcje sprawdzająca czy to kwadrat w tescie