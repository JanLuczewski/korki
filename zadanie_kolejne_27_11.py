# Stwóz klase z pomiarami. MA zawierać pomiary temperatury w Kelvinach oraz date (pomiaru)
# Ma też zawierać funkcję przeliczającą z kelvinów na farenhajty i na celcjusze wykorzystując dekorator property


class Pomiar():
    def __init__(self,num_pom,temp_K):
        self.num_pom = num_pom
        self.temp_K = temp_K

    @property
    def temp_C(self):
        temp_C = self.temp_K - 273
        return temp_C

    @temp_C.setter
    def temp_C(self,value):
        self.temp_K = value + 273



lista_pom = [
    Pomiar('1',300),
    Pomiar('2',311),
    Pomiar('3',294),
    Pomiar('4',311),
    Pomiar('5',320),
]

lista_pom[0].temp_C = 20

print(lista_pom[0].temp_C)

