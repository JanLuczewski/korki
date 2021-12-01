# Zrób zbiór uzytkowników w postaci klasy ,ktora sprawdzi login i haslo wykorzystując for loop
class Uzytkownik():
    def __init__(self,login,haslo,uprawnienia):
        self.login = login
        self.haslo = haslo
        self.uprawnienia = uprawnienia

lista_uzytkownikow = [
    Uzytkownik('Jan','1234','user'),
    Uzytkownik('Karol','4321','user'),
    Uzytkownik('Dorka','cipcia','Pani'),
    Uzytkownik('Kicia','pupcia','Pani'),
]

def verify():
    podaj_login = input('Proszę podaj login: ')
    podaj_haslo = input('Proszę podaj hasło')
    for user in lista_uzytkownikow:
        if podaj_login == user.login and\
           podaj_haslo == user.haslo and\
            print('hej')
           break

verify()

