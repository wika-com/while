m=0
lab=[]
for i in range(7):
    lista=[]
    for j in range(7):
        if i==0 or i==6 or j==0 or j==6:
            lista.append(1)
        else:
            lista.append(0)
    lab.append(lista)
lab[1][2]=1
lab[2][2]=1
lab[2][4]=1
lab[2][5]=1
lab[4][2]=1
lab[4][3]=1
lab[4][4]=1
lab[5][4]=1
lab[5][5]=3
lab[1][1]=2
for k in range(7):
    print(lab[k])
x=1
y=1
o=1
p=1
while o!=5 and p!=5 or m!=20:
    a=input("podaj kierunek: ")
    if a=="w":
        if lab[y-1][x]!=1:
            lab[y-1][x]=2
            lab[y][x]=0
            p=p+1
        elif lab[y-1][x]==1:
            print("Wszedłeś w ścianę")
        m=m+1
    elif a=="s":
        if lab[y+1][x]!=1:
            lab[y+1][x]=2
            lab[y][x]=0
            p=p-1
        elif lab[y+1][x]==1:
            print("Wszedłeś w ścianę")
        m=m+1
    elif a=="a":
        if lab[y][x-1]!=1:
            lab[y][x-1]=2
            lab[y][x]=0
            o=o-1
        elif lab[y][x-1]==1:
            print("Wszedłeś w ścianę")
        m=m+1
    elif a=="d":
        if lab[y][x+1]!=1:
            lab[y][x+1]=2
            lab[y][x]=0
            o=o+1
        elif lab[y][x+1]==1:
            print("Wszedłeś w ścianę")
        m=m+1
    for k in range(7):
        print(lab[k])
if m==20:
    print("Przegrałeś")
else:
    print("Gratulacje! Wygrałeś")