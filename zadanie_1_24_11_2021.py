# Stwórz klasę użytkownika która będzie miała informacje o loginie haśle i o uprawnieniach (admin lub nie)
#   1a)Sprawdz czy użytkownik ma poprawne hasło i login
#   1b)czy jest modem lub adminem.
class Uzytkownik():
    def __init__(self,login,haslo,uprawnienia):
        self.login = login
        self.haslo = haslo
        self.uprawnienia = uprawnienia

lista_uzytkownikow = [
    Uzytkownik('Jan','1234','user'),
    Uzytkownik('Karol','4321','admin'),
]
def verify():
    podaj_nazwe = input('podaj nazwe uzytkownika: ')
    podaj_haslo = input('podaj haslo : ')
    if podaj_nazwe == lista_uzytkownikow[0].login and\
        podaj_haslo == lista_uzytkownikow[0].haslo:
        print(lista_uzytkownikow[0].uprawnienia)
    elif podaj_nazwe == lista_uzytkownikow[1].login and\
        podaj_haslo == lista_uzytkownikow[1].haslo:
        print(lista_uzytkownikow[1].uprawnienia)
        
verify()


