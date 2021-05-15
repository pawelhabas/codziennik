"""
Apka do zajęć codziennych
BY Habas Paweł

TODO    OK  lista zajęć codziennych
TODO    OK Możliwość zaznaczania co jest zrobione
TODO    OK Zapis co dzisiaj zostało zorobione a co nie w pliku
TODO    użycie bazy do nadzoru wykonanych zadań

TODO    usunąć możliwość wykonania czynności 2 razy
TODO    zmienna data powinna być generowana na bierząco a nie z palca
"""

obowiazki_codzienne = ( 'Ćwiczenia', 'Angielski', 'Niemiecki', 'Programowanie')

plik_nazwa = 'dziennik.txt'
data = '2021-05-15'


def czytaj_plik(data):
    tmp = []
    for linia in open(plik_nazwa, encoding='utf-8'):
        if len(linia.strip()) > 0:
            kolumny = linia.strip().split(',')
            if kolumny[0] == data:
                tmp.append(kolumny)
    return tmp


def co_na_dzis(data):
    zrobione = czytaj_plik(data)
    z = []
    for row in zrobione:
        z.append(int(row[2]))
    print(z)
    for o in obowiazki_codzienne:
        # print('o',obowiazki_codzienne.index(o))

        if obowiazki_codzienne.index(o) not in z:
            print(obowiazki_codzienne.index(o), o)


while True:
    for row in czytaj_plik(data):
        print(row)
    print('- - -')
    co_na_dzis(data)
    q = input('Co zrobione (q)? ')
    if q == 'q':
        break
    elif int(q) < len(obowiazki_codzienne):
        print(f'Wykonano "{obowiazki_codzienne[int(q)]}"')
        plik = open(plik_nazwa, encoding='utf-8', mode='a')
        plik.write(f'{data},{obowiazki_codzienne[int(q)]},{q},TAK\n')
        plik.close()
    else:
        print('Brak takiej opcji')
