# decrypter
from langcodr import *
import math
per=input("Enter your message:- ")
trav=0
if per:
    decdm=0
    cod=langcod(per)
    print("coded message= ",cod)
    per2=input("Do you want to decode[y/n]:- ")
    if per2=='y':
        passs=input('Enter the pass word- ')
        if passs=="joel":
            a=cod[::-1]
            cod1=int(a)
            a1=list(a)
            for i in a:
                # print(f"a index({i})- ",trav,end=' ')
                if i.isdigit()==False:
                    a1.remove(i)
                    a=a1[:]
                    continue
                decdm=int(int(i)*math.pow(2,trav))+decdm        
                decdm2=chr(decdm)
                trav+=1
            print(f"\nThe message is= {decdm2}")
            z=input()#for pyinstaller
    else:
        print("Message-: ",cod)
        z2=input()#for pyinstaller