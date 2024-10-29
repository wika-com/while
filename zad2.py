a=[1,2,3],[4,5,6]
b=[10,11],[20,21],[30,31]
macierz=[]
for i in range(len(a)):
    mac1=0
    mac2=0
    for j in range(len(b)):
        c=a[i][j]*b[j][0]
        d=a[i][j]*b[j][1]
        mac1=mac1+c
        mac2=mac2+d
    lista=[]
    lista.append(mac1)
    lista.append(mac2)
    macierz.append(lista)
print(macierz)