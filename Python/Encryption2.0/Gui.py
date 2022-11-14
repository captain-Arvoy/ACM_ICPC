import tkinter as tk
from tkinter.messagebox import showinfo
def bin(var):
    if var<0:
        return
    return bin(var%2)

def main_window():
    t_ob1=tk.Tk()
    t_ob1.title("Ardrepter")
    a=tk.StringVar(t_ob1)
    t_ob1.geometry("600x400")
    tk.Label(t_ob1,text='Enter your message: ').grid(padx=5,pady=3,row=2,column=0)
    tk.Entry(t_ob1,textvariable=a).grid(padx=20,pady=3,row=2,column=1)
    tk.Button(t_ob1,text="Enter",fg="white",bg="blue",command=t_ob1.destroy).grid(padx=3,pady=2,row=5,column=4)
    t_ob1.mainloop()
    # showinfo("Confirmation window",message=f"your message is\"{a.get()}\"")#for debugging
    return a.get()
text=main_window()
print(f"{text}")
encr=[]
for i in text:
    encr.append(ord(i))
