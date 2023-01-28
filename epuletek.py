from Epulet import Epulet
epulet_lista = []
def beolvas():
    f = open('epulet.txt', 'r',encoding='utf-8')
    f.readline().strip()
    sorok = f.readlines()
    f.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        epulet_lista.append(Epulet(sor))
        i += 1
    print(epulet_lista[0])

def epuletek_szama():
    return len(epulet_lista)

def konzolra_kiir():
    print('III/A, B')
    print(f'\tAz épületek száma: {epuletek_szama()}')

def legmagasabb():
    i = 0
    db = 0
    while i < len(epulet_lista):
        if epulet_lista[i].getmagassag()*3.28 > 555:
            db += 1
        i += 1
    print('III/C:')
    print(f'\tAz 555 lábnál magasabb épületek száma: {db}')

def legoregebb():
    i = 0
    index = 0
    while i < len(epulet_lista):
        if epulet_lista[index].ev > epulet_lista[i].ev:
            legoregebb = epulet_lista[i].ev
            index = i
        i += 1
    print('III/D:')
    print(f'\tA legöregebb épület országa: {epulet_lista[index].orszag}')