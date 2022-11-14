m,ms,n,ns=[],[],[],[]
for i in range(3):
    n,ns=[],[]
    for j in range(3):
        i1=int(input('Enter an element'))
        n.append(i1)
        ns.append(i1**2)
    m.append(n)
    ms.append(ns)  
print("The matrix:-")
for i in range(3):      
    for j in range(3):
        print(m[i][j],end=' ')
    print()
print("The square of elements matrix:-")
for i in range(3):
    for j in range(3):
        print(ms[i][j],end=' ')
    print()   
            