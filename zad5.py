a=int(input("Podaj liczbę dodatnią: "))
i=2
suma=0
m=0
k=1
while suma<=a:
    m=0
    for j in range(2,i):
        if i%j==0:
            m=m+1
    if m==0:
        suma=suma+i
        k=k+1
    i=i+1
suma=suma-i
k=k-1
print(suma,k)
