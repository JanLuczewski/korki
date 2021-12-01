# Stwóz klase z pomiarami. MA zawierać pomiary temperatury w Kelvinach oraz date (pomiaru)
# Ma też zawierać funkcję przeliczającą z kelvinów na farenhajty
# Ma zwrócić pomiar z największą temperaturą

class Pomiar():
    def __init__(self,numer_pom,temp_K):
        self.numer_pom = numer_pom
        self.temp_K = temp_K
    def przel_F(self):
        temp_F = ((self.temp_K - 273.15) * 1.8) + 32
        return temp_F
    def przel_C(self):
        temp_C = self.temp_K - 273
        return temp_C


lista_pom = [
    Pomiar('1',300),
    Pomiar('2',311),
    Pomiar('3',294),
    Pomiar('4',311),
    Pomiar('5',320),
]

def wypluj():
    podaj_numer = input('Podaj numer pomiaru: ')
    for pomiar in lista_pom:
        if podaj_numer == pomiar.numer_pom:
            jaka_jedn = input('Podaj w jakiej jednostce chcesz wynik: C/F/K')
            if jaka_jedn == 'C':
                print(f'oto wynik w celcjuszach :{pomiar.przel_C()}')
            elif jaka_jedn == 'F':
                print(f'oto wynik w farenheitach :{pomiar.przel_F()}')
            elif jaka_jedn == 'K':
                print(f'Oto wynik w kelvinach: {pomiar.temp_K}')
            else:
                print('Zły wybór')



# ℉ =(K - 273.15)* 1.8000+ 32.00
wypluj()