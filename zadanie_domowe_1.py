# 1
# "konto" jest słownikiem w któym mam ująć takie informacje jak login,hasło,data urodzenia,mejl
#     1A)zrób funckję zalogowania które będzie weryfikowało hasło -czy się zgadza dla danego konta
#     1B) czyszczenie wartości przypisanej do klucza -"wyczyść hasło"

konto_1 = {
    'login':'Jan',
    'haslo':'1234',
}
konto_2 = {
    'login':'Karol',
    'haslo':'4321',
}
def logowanie():
    podaj_login = input('podaj login:  ')
    podaj_haslo = input('podaj haslo:  ')
    usun_haslo = input('czy chcesz usunąć hasło ? : ')
    if podaj_login == konto_1['login'] and\
       podaj_haslo == konto_1['haslo']:
        print(f'witaj {konto_1["login"]}')
        if usun_haslo == 'y':
            del konto_1['haslo']
            print(konto_1)

    elif podaj_login == konto_2['login'] and\
         podaj_haslo == konto_2['haslo']:
         print(f' hej {konto_2["login"]}')
         if usun_haslo == 'y':
            konto_2['haslo'] = ''
            print(konto_2)
    else :
        print('żegnam')

konto_1['data_urodzenia'] = '1992-11-25'
konto_1['adres_mejlowy'] = 'jan@gmail.com'
konto_2['data_urodzenia'] = '11-05-1994'
konto_2['adres_mejlowy'] = 'huj@kutas.com'



logowanie()









