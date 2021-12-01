def pole_prostokata(bok1,bok2):
    if type(bok1) == str or\
        type(bok2) == str:
        return 'bez stringow prosze'
    pole = bok1 * bok2
    return pole
def czy_kwadrat(bok1,bok2):
    if type(bok1) != int or\
        type(bok2) != int:
        return 'podane wartosci NIE sa liczbowe'
    if bok1 == bok2:
        return 'to jest kwadrat'
    else:
        return 'to nie jest kwadrat ty gamoniu'



