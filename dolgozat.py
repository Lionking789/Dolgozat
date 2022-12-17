import random

def beker():
    szam = input("Kérek egy páros számot! ")
    i = 0
    while not (szam % 2 == 0):
        szam = input("Ez nem PÁROS!Páros számot kérek! ")
    if szam % 2 ==0:
        print(f"{szam} páros")
    else:
        print(f"{szam} páratlan")


def masodik():
    szam = int(input("Kérek az 1. páros számot! "))
    while not (szam % 2 == 0):
        szam = input("Ez nem PÁROS!Páros számot kérek! ")
        szam = input("Kérem a 2.páros számot")
        szam = input("Kérem a 3. páros számot")

    if szam % 2 == 0:
        print(f"{szam} páros")
    else:

     print(f"{szam} páratlan")














