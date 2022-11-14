import math,random
with open("pass.txt","a+",newline='') as fh:
    # n=int(input("enter the digits of passwords:-"))
    # p=math.pow(10,n)
    ps1=int(random.randint(1,3))
    ps=str(ps1)
    a1=fh.read()
    if ps not in a1:
        print(ps)
        fh.write(ps)
import math,random
with open("pass.txt","a+",newline='') as fh:
    # n=int(input("enter the digits of passwords:-"))
    # p=math.pow(10,n)
    ps1=int(random.randint(1,3))
    ps=str(ps1)
    a1=fh.read()
    if ps not in a1:
        print(ps)
        fh.write(ps)