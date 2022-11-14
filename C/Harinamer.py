import time
import os
from tkinter.messagebox import askyesno, showinfo
var=0
k=1
def chant(var):
    mal=["O" for i in range(54)]
    st="Hare krsna Hare krsna Krsna Krsna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare"
    st2=list(st)
    panch="namo om vishnoh padaya krsna preshthaya bhutale srimati bhaktivedanta swamini iti namine namaste saraswate gaura vani pracharine nir vishesh shunya wadi paschateya\
desh tarine\njai sri krsna chaitanya prabhu nityananda sri advaita gadadhara sriwasadi gaura bhakta vrinda"
    panc=list(panch)
    print(f"\t\t\t\t\t\t\t   .   ")
    for i in range(1,27):
        print(f"\t\t\t\t\t\t\t{mal[54-i]}      {mal[i]}")
    print(f"\t\t\t\t\t\t\t   {mal[27]}   ") 
    for z in panc:
        print(z,end='')
        time.sleep(0.07)
    print('\n')
    os.system('cls')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def hear():
        for j in st2:
            print(j,end="")
            time.sleep(0.07)
        print("\n\n")
        if (k>53):
            reply=askyesno(title='Computer',text='Shall we go to next round?')
            if var<2 and reply:
                chant(var+1)
            else:
                showinfo(title='computer',text='today\'s round finished!\nHARIBOOOLLLL!!!')
                return 0
        time.sleep(1)
        os.system('cls')
        return 1
    def mala():
        global k
        repl=1
        while repl:
            mal[k]="."
            print(f"\t\t\t\t\t\t\t   {mal[0]}   ")
            for i in range(1,27):
                print(f"\t\t\t\t\t\t\t{mal[54-i]}      {mal[i]}")
            print(f"\t\t\t\t\t\t\t   {mal[27]}   ")    
            mal[k]="O"
            k+=1
            repl=hear()

    mala()
    hear()
chant(0)