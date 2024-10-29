from random import randint
from random import seed
x=1
a=randint(0,100)
b=int(input("Podaj liczbę: "))
while b!=a:
    x=x+1
    if b>a:
        print("za duża")
    elif b<a:
        print("za mała")
    b=int(input("Podaj liczbę: "))
print("Gratuluję! Zgadłeś liczbę po", x, "próbach")