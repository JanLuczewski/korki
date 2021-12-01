def dodaj_klucz(slownik,klucz,wartosc):
    slownik[klucz] = wartosc

osoba = {
    "imie": 'Jan',
    'nazwisko':'Luczewski'
}
print(osoba["imie"])
osoba["imie"] = 'Piotr'
osoba['nazwisko'] = 'Co jest hujem'
print(osoba['imie'])
print(osoba['nazwisko'])

osoba['numer tel'] = '0700'
print(osoba['numer tel'])
print(osoba)

dodaj_klucz(osoba,"wzrost","180")
print(osoba)

# 1
# "konto" jest słownikiem w któym mam ująć takie informacje jak login,hasło,data urodzenia,mejl
#     1A)zrób funckję zalogowania które będzie weryfikowało hasło -czy się zgadza dla danego konta
#     1B) czyszczenie wartości przypisanej do klucza -"wyczyść hasło"
# 2.
# baza osób w której lista osób skłąda się ze słowników gdzie 1 słownik to jedna osoba.
#     2A) zrób funkcję liczącą ilość Andrzejów
#     2B) zrób funkcję która zmieni imie każdewgo użytkowanika na Andrzej


