# Stwórz klase pomiar która będzie zawierać numer pomiaru , temp w  C i nazwe
# (czujnika).Stwóz funkcję która wyświetli wszystkie pomiary dla danego czujnika.
# *Argumentem funkcji będzie nazwa czujnika i lista pomiarów.

class Pomiar():
    def __init__(self,num_pom,temp_C,naz_czuj):
        self.num_pom = num_pom
        self.temp_C = temp_C
        self.naz_czuj = naz_czuj

lista_pomiarow = [
    Pomiar('1',43,'Lajka'),
    Pomiar('2',44,'Lajka'),
    Pomiar('3',39,'Lajka'),
    Pomiar('4',12,'Bajka'),
    Pomiar('5',23,'Bajka'),
    Pomiar('6',45,'Czajka'),

]

def wypluj_pom():
    podaj_nazwe = input('podaj nazwe czujnika:Lajka/Bajka/Czajka: ')
    for pomiar in lista_pomiarow:
        if podaj_nazwe == pomiar.naz_czuj:
            print(f'oto wyniki dla wybranego czujnika: {pomiar.temp_C}')
        else:
            pass


wypluj_pom()




