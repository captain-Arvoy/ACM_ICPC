import math,random
def langcod(a):
    p=["!","@","#","$","%","&","*","(",")","_","+"]
    c=1
    gr=''
    for i in a:
        j=ord(i)
        n=j
        while n>0:
            if c%2==0:
                gr=gr+random.choice(p)
            rem=n%2    
            gr=str(rem)+gr
            n=n//2
        c+=1
    return gr
# decrypter
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
            # cod1=int(a)
            a1=list(a)
            decdm2=''
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