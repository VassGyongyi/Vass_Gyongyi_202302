import random
veletlen_lista = []
def sorozat_feldolgozas():
    i = 0
    while i < 7:
        vel = random.randint(0,1)
        veletlen_lista.append(vel)
        i += 1
    #print(veletlen_lista)
    j = 0
    kimenet =" "
    ertek = " "
    while j < len(veletlen_lista):
        if veletlen_lista[j] == 0:
            ertek = "ÍRÁS"
        else:
            ertek = "FEJ"
        if j == len(veletlen_lista)-1:
            kimenet += ertek
        else:
            kimenet += ertek + "-"
        j += 1
    print('II/A, B, C:')
    print(f'\t{kimenet}')

def fejek_szama():
    i = 0
    db = 0
    while i < len(veletlen_lista):
        if veletlen_lista[i] == 1:
            db += 1
        i += 1
    return db

def konzol_kiir():
    print('II/D, E:')
    print(f'\tA fejek száma: {fejek_szama()}')

def file_kiir():
    f=open('fejek.txt','w',encoding='utf-8')
    f.write('II/F:')
    f.write(f'\n\tA fejek száma: {fejek_szama()}')
    f.close()