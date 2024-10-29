A=[1,2,3],[4,5,6]
At=[]
for i in range(len(A[0])):
    a=A[0][i]
    b=A[1][i]
    print(a,b)
    lista=[]
    lista.append(a)
    lista.append(b)
    At.append(lista)
print(At)

