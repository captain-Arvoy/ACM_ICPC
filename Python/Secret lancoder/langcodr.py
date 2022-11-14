# To encode message in binary form
# a=input("Enter your message:- ")
import random
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
    # # gr=''
    # per=input('Do you want to decrypt it[y/n]:- ')
    # if per=='y':
    #     print(gr)
    #     # import decryter