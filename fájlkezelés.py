def beolvas(fajlnev):
    fajlom = open("stadionok.txt.","r", encoding='utf-8')
    print(fajlom)
    # fajl_tartalma=fajlom.read()
    # print(fajl_tartalma)
    fejlec = fajlom.readline().strip()
    print(fejlec)
    # sor = fajlom.readline().strip()
    # print(sor)
    sorok = fajlom.readlines()
    print(sorok)
    feldolgoz(sorok)
    fajlom.close()

stadionnev=[]
helyszin=[]
csapatszam=[]
elso=[]
utolso=[]

def feldolgoz(sorok):
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(";")
        print(sor)
        stadionnev.append(sor[0])
        helyszin.append(sor[1])
        csapatszam.append(sor[2])
        elso.append(sor[3])
        utolso.append(sor[4])
        i += 1

    print(stadionnev)
    print(helyszin)
    print(csapatszam)
    print(elso)
    print(utolso)

def adat():
    len(stadionnev)
    print(f"A stadion neve: Metropolitan Park")

def hely():
    len(helyszin)
    print(f"A stadion helyszínének városa: New York")

def csapat():
    len(csapatszam)
    print(f"A stadionnak hányas csapata: 1")

def palya1():
    len(elso)
    print(f"Mikor léptek előszőr pályára: pl.: 1984-05-13")

def palya2():
    len(utolso)
    print(f"Mikor léptek utoljára pályára: pl.: 1985-08-23")