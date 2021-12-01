# Stwóz klase z pomiarami. MA zawierać pomiary temperatury w Kelvinach oraz date (pomiaru)
# Ma też zawierać funkcję przeliczającą z kelvinów na celsjusze
# Ma zwrócić pomiar z największą temperaturą
class Pom():
    def __init__(self,numerek,temp_K,data_pom):
        self.numerek = numerek
        self.temp_K = temp_K
        self.data_pom = data_pom
        self.temp_C = None
    def zamiana_na_c(self):
        self.temp_C = self.temp_K
        self.temp_C -= 273
        return self.temp_C



lista_pom1 = [
    Pom('1',300,'20-11-2021'),
    Pom('2',311,'21-11-2021'),
    Pom('3',294,'22-11-2021'),
    Pom('4',311,'23-11-2021'),
    Pom('5',320,'24-11-2021'),
]
lista_pom2 = [
    Pom('1',389,'25-11-2021'),
    Pom('2',290,'26-11-2021'),
    Pom('3',293,'27-11-2021'),
    Pom('4',330,'28-11-2021'),
    Pom('5',299,'29-11-2021'),
]

def przelicznik():
    podaj_numer = input('podaj numer pomiaru: ?')
    for pomiar in lista_pom:
        if podaj_numer == pomiar.numerek:
            print(f"oto temperatura w Celcjuszach: {pomiar.zamiana_na_c()}")

def maximum(lista):
    najwyzsza = 0
    for pomiar in lista:
        if pomiar.temp_K > najwyzsza:
            najwyzsza = pomiar.temp_K
    return najwyzsza


# przelicznik()
print(maximum(lista_pom2))



