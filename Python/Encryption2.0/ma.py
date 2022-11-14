import time
import os
k=1
mal=["O" for i in range(54)]
def mala():
    print(f"   {mal[0]}   ")
    for i in range(1,27):
        print(f"{mal[54-i]}      {mal[i]}")
    print(f"   {mal[27]}   ")    
i=108
st="Hare krsna Hare krsna Krsna Krsna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare"
st2=list(st)
while i>0:
    for j in st2:
        # print(j,end="")
        # time.sleep(0.02)
        pass
    print("\n\n")
    if (k>54):
        break
    mal[k]="."
    mala()
    mal[k]="O"
    k+=1
