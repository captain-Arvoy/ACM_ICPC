import string
from xmlrpc.client import boolean



def Listu():
    wordinput_var=input("Enter a word: ")
    lis=[]
    while bool(wordinput_var) is True:        
        lis.append(wordinput_var)
        wordinput_var=input("Enter a word: ")
    print("Sorting List of words...")
    for i in range(100000000):
        pass
    print("user input list-: ",lis)
    a=sor(lis)
    print("sorted list-: ",a)
    return a
def sor(clien_word):
    if bool(clien_word) is True:
        for i in range(len(clien_word)):
            for j in range(len(clien_word)-i-1):
            # chose=input("Do you want to arrange in\n i) ascending order\n ii) descending order ")           
            # if chose=='i':
                if len(clien_word[j])>len(clien_word[j+1]):
                    t=clien_word[j+1]
                    clien_word[j+1]=clien_word[j]
                    clien_word[j]=t
            # # elif chose=='ii':
            #     if len(clien_word[j])<len(clien_word[j+1]):
            #         t=clien_word[j]
            #         clien_word[j]=clien_word[j+1]
            #         clien_word[j+1]=t
    return clien_word
def search_word(l,cheklist):
    print("Searching...")
    for i in range(100**3):
        pass
    print("cheklist= ",cheklist)
    i,j=0,len(cheklist)-1
    if l in cheklist:
        while i<j:
            mid=(i+j)//2
            print(mid)
            if len(cheklist[mid])<len(l):
                i=mid+1
            elif len(cheklist[mid])>len(l):
                j=mid-1
            elif cheklist[mid]==l:
                return cheklist[mid],'at',mid+1,'in sorted list'       
    else:
        return "The searched word is not present in the list:("       
#_main_
ch=True
while ch !='3' and ch is True:
    List2=""
    ch=input("Enter your choice-\n1.To enter list of words \n2.To search a word\n3.Exit\n")            
    if ch=='1':
        List2=Listu()
        sear_word=input("Enter word to search in the list: ")
        if bool(sear_word) is True and bool(List2) is True:
            res=search_word(sear_word,List2)
            print("The word is",res) 
        else:
            ch=None       
    elif ch=='2':
        if List2 is True:
            sear_word=input("Enter word to search in the list: ")
            search_word(sear_word,List2)
        else:
            print("First enter a list to search, do you want to continue?")
            confirmation=input()
            if confirmation=='yes':
               ch=True
               continue

                

                 
                    
    
