import math


def pitagoras(A,B):
    x = A**2 + B**2
    C = math.sqrt(x)
    return C


if __name__ == "__main__":
    wynik = pitagoras(3,4)
    wynik2 = wynik*3
    print(wynik)
    print(wynik2)
    




