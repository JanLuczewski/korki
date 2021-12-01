# 2.
# baza osób w której lista osób skłąda się ze słowników gdzie 1 słownik to jedna osoba.
#     2A) zrób funkcję liczącą ilość Andrzejów
#     2B) zrób funkcję która zmieni imie każdewgo użytkowanika na Andrzej
konto_1 = {
    'login':'Jan',
    'haslo':'1234',
}
konto_2 = {
    'login':'Karol',
    'haslo':'4321',
}
konto_3 = {
    'login':'Andrzej',
    'haslo':'1111',
}
lista_kont = [konto_1,konto_2,konto_3]
def licznik_andrzejow():
    licznik = 0
    for konto in lista_kont:
        if konto['login'] == 'Andrzej':
            licznik += 1
    print(licznik)

def tranformacja():
    for konto in lista_kont:
        if konto['login'] != 'Andrzej':
            konto['login'] = 'Andrzej'

tranformacja()
licznik_andrzejow()

