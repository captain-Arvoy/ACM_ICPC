import csv
import math,random
with open("G:\\python\\passexperi.txt","a+",newline='') as fh:
    n=int(input("enter the digits of passwords:-"))
    p=math.pow(10,n)
    ps1=int(random.random()*p)
    ps=str(ps1)
    a1=fh.read()
    ps2=''
    c=0
    p=['!','@','#','$','%','^','&','*','_']
    for i in ps:#experimental
        if c%2==0:
            i0=int(i)
            i01=chr(i0)
            ps2=ps2+random.choice(p)
        else:
            ps2=ps2+i
        c+=1
    with open("acnt names.txt","a+",newline='') as fh2:
        ac=csv.writer(fh2)
        chk=csv.reader(fh2)
        if ps2 not in chk:       
            print(ps2)
            acnm=input("Enter the account name-: ")
            acdetails=[acnm,ps2]
            print(acdetails)
            ac.writerows(acdetails)
            fh.write(acnm)
            fh.write("- ")
            fh.write(ps2)
            fh.write("\n")
        else:
            print("pass nahi")     
        ps2,ps='','' 