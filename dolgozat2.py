import random

lista = veletlen_szamok(lista)
ketjegyuek_szama=(lista)
parososszeg = paros_osszege(lista)
paratlanosszeg = paratlan_osszege(lista)
import random

def veletlenszamok():
    # [-40, 150 ] közötti véletlen számok

    if parososszeg > paratlanosszeg:
        print(f"A páros számok öszege nagyobb mint a páratlan számok összege! ({parososszeg} > {paratlanosszeg})")
    else:
        print(f"A páratlan számok öszege nagyobb mint a páros számok összege! ({paratlanosszeg} > {parososszeg})")


def veletlen_szamok(lista):
        i = 1
        lista = []
        while i <= 13:
            vel = int(random.random() * 190) - 40
            lista.append(vel)
            i += 1
        print(lista)
        return lista

def ketjegyuek_szama(lista):
        i = 0
        ketjegyuDb = 0
        while i < len(lista):
            if lista[i] >= 10 and lista[i] < 100:
                ketjegyuDb += 1
            i += 1

        print(f"A kétjegyüek száma: {ketjegyuDb}. db")
        return ketjegyuDb

def paros_osszege(lista):
        i = 0
        osszeg = 0

        while i < len(lista):
            if lista[i] % 2 == 0:
                osszeg += lista[i]
            i += 1

        print(f"A páros szűmok összege: {osszeg}")
        return osszeg

def paratlan_osszege(lista):
        i = 0
        osszeg = 0

        while i < len(lista):
            if not (lista[i] % 2 == 0):
                osszeg += lista[i]
            i += 1

        print(f"A páratlan számok összege: {osszeg}")
        return osszeg