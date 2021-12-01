# Stwóz klase z pomiarami. MA zawierać pomiary temperatury w Kelvinach oraz date (pomiaru)
# Ma też zawierać funkcję przeliczającą z kelvinów na farenhajty
# Ma zwrócić pomiar z największą temperaturą
class Pomiar():
    def __init__(self,num_pom,temp_K):
        self.num_pom = num_pom
        self.temp_K = temp_K
    def przel_na_C(self):
        temp_C = self.temp_K -273
        return temp_C
    def przel_na_F(self):
        temp_F = ((self.temp_K - 273.15) * 1.8) + 32
        return temp_F

lista_pomiarow = [
Pomiar('1',300),
    Pomiar('2',311),
    Pomiar('3',294),
    Pomiar('4',311),
    Pomiar('5',320),
]

def wypluj():
    podaj_numer = input('podaj numer pomiaru')
    for pomiar in lista_pomiarow:
        if podaj_numer == pomiar.num_pom:
            podaj_przelicznik = input('w jakiej jednostce chcesz wynik? C/K/F')
            if podaj_przelicznik == 'C':
                print(f'Oto temperatura w celcjuszach:{pomiar.przel_na_C()}')
            elif podaj_przelicznik == 'K':
                print(f'Oto temperatura w kelvinach:{pomiar.temp_K}')
            elif podaj_przelicznik == 'F':
                print(f'Oto temperature w farenheitach:{pomiar.przel_na_F()}')
            else:
                print('błędny wybór')


wypluj()
