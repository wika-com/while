
a=int(input("Podaj liczbę: "))
lista=[]
while a>0:
    lista.append(a%2)
    a=a//2
print(lista.reverse())
