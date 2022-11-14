import math
def debig(X,K):
            b=(X-1)
            d=int(math.pow(b,2))+4*K
            t1=(-b+int(math.sqrt(d)))//2
            t2=(-b-int(math.sqrt(d)))//2
            if t1>0:
                T=t1
                return T
            if t2>0:
                T=t2
                return T
#main
a=int(input('Enter:- '))
b=int(input('Enter:- '))
print('result- ',debig(a,b))