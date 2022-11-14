
import random
from tkinter.messagebox import showinfo 
a=set()
start=309
end=350
length=end-start+1
while (3):
    prog=(len(a)/length)*100
    input('Ready?')
    b=random.randint(start,end)
    print("%s"%b)
    if b in a:
        pass
    else:
        a.add(b)
    if len(a)==length:
        showinfo("checkmark","DONE!")
        break
    elif prog%10<=1:
        showinfo("checkpoint","%s"%prog)
