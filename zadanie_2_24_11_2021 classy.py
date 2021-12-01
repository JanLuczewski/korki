# Zrób zbiór uzytkowników w postaci klasy ,ktora sprawdzi login i haslo wykorzystując for loop


class Uzytkownik():
    def __init__(self,login,haslo,uprawnienia):
        self.login = login
        self.haslo = haslo
        self.uprawnienia = uprawnienia

lista_uzytkownikow = [
    Uzytkownik('Jan','1234','user'),
    Uzytkownik('Karol','4321','user'),
    Uzytkownik('Pies','hauhau','mod'),
    Uzytkownik('Kicia','miaumiau','admin'),
]

def verify():
    podaj_login = input('podaj nazwe uzytkownika')
    podaj_haslo = input('podaj haslo')
    for user in lista_uzytkownikow:
        if podaj_login == user.login and\
            podaj_haslo == user.haslo and \
            (user.uprawnienia == 'admin' or\
            user.uprawnienia == 'mod'):
            print(f'witaj {user.login}')
            break
    if podaj_login == lista_uzytkownikow[1].login:
        print('Karol huj')


verify()


