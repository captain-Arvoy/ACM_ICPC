import random
from tkinter.messagebox import showinfo, showwarning
import mysql.connector as c
import tkinter as t
root=t.Tk()
root.title('Developer confirmation window')
root.geometry('1000x300')
def retry():
    print('.......Restarting connection.....')
    for i in range(10001):
        print(i//100,'%',end='\r')
    showinfo("sql connectivity",'Database connected')
    print("Enter database credentials...")
    global hst,usr,passe,db
    try:
        hst=input('Enter host name: ')
        usr=input('Enter the user name: ')
        passe=input('Enter the password: ')
        db=input('Enter the database: ')
        print("connecting...")
        con=c.connect(host=f'{hst}',user=f'{usr}',password=f'{passe}',database=f'{db}',autocommit=True)
        if con.is_connected():
            root2.wm_deiconify()
            showinfo('database connector','Successfully connected')
            root2.wm_withdraw()
        curso=con.cursor()
        sql='drop table if exists employee;'
        curso.execute(sql)
        sql="Create table employee(S_no integer(5) primary key,nme varchar(75),age integer,gender char(75),designation varchar(70),salary integer(75));"
        curso.execute(sql)
    except:
        # root2.wm_deiconify()
        showwarning('Database connetor','   Invalid credentials   ')
        # root2.wm_withdraw()
        retry()

def screen():
    a=t.Label(root,text='Are you Developers',font=('segoe print',20))
    b=t.Button(root,text='Yes',padx=20,pady=15,command=man,bg='yellow',fg='blue')
    c1=t.Button(root,text='No',padx=20,pady=15,command=man2,bg='yellow',fg='blue')
    a.pack(anchor='n',side='top',fill="x")
    b.pack(anchor='center',side='top',fill='x')
    c1.pack(anchor='center',side='top',fill='x')
    d.pack(anchor='center',side='top',fill='x')
def man():
    root.destroy()
    global hst
    hst='yo'
    
    
def man2():
    root.destroy()
    global hst
    hst='no'


hst=screen()
root.mainloop()
root2=t.Tk()
root2.wm_withdraw()
if hst=='yo'or hst=='yes' or hst=='y' or hst=='[y]' or hst=='yep':
    print('Welcome....To EDMS(Employee data  management system)....\nLogging you in Mr.Ard and Mr.Chinmay :)\n')
    hst='localhost'
    usr='root'
    passe='12345678'
    db='test'
    for i in range(2000**2+50000):
        pass
else:
    print('Welcome....To EDMS(Employee data  management system)....\nplease enter your database credentials')
    hst=input('Enter host name: ')
    usr=input('Enter the user name: ')
    passe=input('Enter the password: ')
    db=input('Enter the database: ')
    try:
        con=c.connect(host=f'{hst}',user=f'{usr}',password=f'{passe}',database=f'{db}',autocommit=True)
    except:
        root2.wm_deiconify()
        showwarning('Database connetivity error','Invalid credentials')
        root2.wm_withdraw()
        retry()
con=c.connect(host=f'{hst}',user=f'{usr}',password=f'{passe}',database=f'{db}',autocommit=True)
curso=con.cursor()
sql='drop table if exists employee;'
curso.execute(sql)
sql="Create table employee(S_no integer(5) primary key,nme varchar(75),age integer,gender char(75),designation varchar(70),salary integer(75));"
curso.execute(sql)
#-----------------Table created------------------------------------------------------------------------------------------------------
wish=input('switch to present mode sir?\n')
if wish=='yo'or wish=='yes' or wish=='y' or wish=='[y]' or wish=='yep':
    nam1=['Yashoda','Dhruv','Abhay']
    midnm=['nandan','vishnu','Aditya']
    las=['dasa','Roshan','kishor']
    i=0
# lalala lori dudh ki katori dudh mein batasha......mamma ne mujhe data 
    gen=['M','F']
    desgn=['Team coordinator','CEO','Product supervisor','Programmer','Trainer','script writer','Reporter','support','legal advisor','travel agent']
    while i<300:
        age=random.randint(18,35) 
        sal=int(random.random()*10000)+2356
        rndf=random.choice(nam1)
        rndm=random.choice(midnm)
        rndl=random.choice(las)
        nam=rndf+' '+rndm+' '+rndl
        gen2=random.choice(gen)
        desegn2=random.choice(desgn)
        desegn2=desegn2.upper()
        sql3=f"insert into employee values({i+1},'{nam}',{age},'{gen2}','{desegn2}',{sal});"
        curso.execute(sql3)
        i+=1
        if i<100:
            print(f'loading {i//3}%',end='\r')
        elif i>100:
            print(f'loading {i//3}%',end='\r ')
#--------------------------database created----------------------------------------------------------------------------------------------------------------------------------------      
def newemployee():
    root2.wm_withdraw()
    if con.is_connected():
        print('\rConnection established')
    else:
       pass
    sql='select max(S_no)"entry" from employee;'
    curso.execute(sql)
    s_no=curso.fetchall()
    sno=s_no[0][0]
    siz=int(input('Enter number of employees to enter: '))
    for i in range(siz):
       sno+=1      
       try:
            nam=input('Enter the name of the employee:')
            age=int(input('Enter the age of the person:'))
            gen=input('Enter the gender of the person:')
            desegn=input('Enter the designation of the employee:')
            desegn=desegn.capitalize()
            sal=int(input('Enter the salary of the employee:'))
            sql3=f"insert into employee values({sno},'{nam}',{age},'{gen}','{desegn}',{sal});"
            print(f"inserted.")
            curso.execute(sql3)
       except Exception as e:
            showwarning('Input error',f'{e}')
            print("------cancelling entry-------")
            if i<siz:
                continue
    
def employeeview():
    root2.wm_withdraw()    
    user=input('\rEnter your username for database access: ')
    passw=input('Enter pin: ')
    if user=='admin21' and passw=='15987':
        print('Authentication verified...\n ')
    else:
        root2.wm_deiconify()
        showwarning('Authentication error','INCORRECT USER OR PASSWORD DETAILS')
        print("reloading....")
        root2.wm_withdraw()
        employeeview()
    usein=input('Enter the username: ')
    while usein=='cheat':
        print(nam)
        usein=input('Enter the username: ')
    data=f"select * from employee where nme='{usein}'"
    curso.execute(data)
    dat=curso.fetchall()
    if dat:
        for i in dat:
            print(i)
    else:
        root2.wm_deiconify()
        showwarning('database exception','No employee by this name exists in database')
        root2.wm_withdraw()
        
    
def employee_editor():
    root2.wm_withdraw()
    user=input('\rEnter your username for database access: ')
    passw=input('Enter pin: ')
    if user=='admin21' and passw=='15987':
        print('Authentication verified')
    else:
        root2.wm_deiconify()
        showwarning('Authentication error','INCORRECT USER OR PASSWORD DETAILS')
        print("reloading....",end='\r')
        employee_editor()
    dat=[]
    p=0
    prin=t.Tk()
    prin.wm_withdraw()
    def retr():
        par=input('How you want to search by\n name,by gender,\nby designation,\nby salary')
        if par=='salary':
            rng=t.Tk()
            a=t.Label(text='Max salary of employee: ')
            a.grid(row=3,column=0)
            a2=t.Entry()
            a2.grid(row=3,column=1)
            b=t.Label(text='Minimum salary of the employee')
            b.grid(row=4,column=0)
            b2=t.Entry()
            b2.grid(row=4,column=1)
            sub=t.Button(text='Enter',bg='blue',fg='white',command=rng.destroy)
            sub.grid(row=6,column=6)
            rng.mainloop()
            mx=a2.get()
            mn=b2.get()
        empnm=input(f'Enter the {par} of the employee: ')
        if int(empnm):
            sql=f"Select * from employee where {par}={empnm}"
            curso.execute(sql)
        else:
            sql=f"Select * from employee where {par}='{empnm}'"
            curso.execute(sql)
        dat=curso.fetchall()
        global p,ac
        ac=0
        if dat:
            prin.wm_deiconify()
            print()
            t.Label(prin,text='S_no ,nme                    ,age,gender,designation ,salary ')
            ac+=1
            for p in dat:
                t.Label(prin,text=f"'{ac}.   '{p}").grid(row=ac)
                proc=input('press any key to proceed,\t\'stp\'to stop')
                if proc=='stp':
                    break
                ac+=1
                continue
        else:
            showwarning('Data error','No employee found')
            retr()
    retr()
    e_inf=input('Which info you want to change?\n')
    e_inf_no=int(input('Which number employee you want to change?\n '))
    cng=eval(input(f'you want to change {e_inf}of {e_inf_no}th employee on the screen --->[?] :\n'))
    fecher = dat[e_inf_no-1][1]
    pull=f"select {e_inf} from employee where nme={fecher}"
    pulled=curso.execute(pull)
    print(pulled)
    if int(cng):
        push=f"update employee set{e_inf}={cng}where nme={fecher}"
        curso.execute(push)
        curso.execute(f"select{e_inf} from employee where nme={fecher}")
        print('updated-',curso.fetchall())
    else:
        push=f"update employee set{e_inf}='{cng}'where nme={fecher}"
        curso.execute(push)
        curso.execute(f"select{e_inf} from employee where nme={fecher}")
        print('updated-',curso.fetchall())
    prin.mainloop()

#main
choice=1
pop=t.Tk() # why we haven't intialised this line in the beginning because if we do so then python would make the tk window without
# packing the widgets in the while loop basically I have to create the window after the native verification window 
db=t.Tk()
db.title('database')
db.geometry("600x400")
db.wm_withdraw()
def exi():
    pop.destroy()
    showinfo('Devolopers message','Thank you for choosing EDMS, Give us Full marks! XD')
    global choice
    choice=False
    root2.destroy()
while choice:
    def opndb():
        db.wm_deiconify()
        d.grid_forget()
        curso.execute('select * from employee')
        dat=curso.fetchall()
        # print(dat)
        rw=0
        for i in dat:
            i1=i
            t.Label(db,text=f'{i1}').grid(row=rw,column=0,padx=15,pady=3)
            rw+=1
#X_X meri band baj gayi hai.....aur nahi ho sakta kal se JEE meri Jaan
    def one():
        pop.destroy()
        newemployee()
    def two():
        pop.destroy()
        employeeview()
    def three():
        pop.destroy()
        employee_editor()
    t.Label(pop,text='Click your choice',fg='red',font='Nougat').grid(row=5,column=15,padx=25,pady=7)
    t.Button(pop,text='1.Register employee',command=one,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
    t.Button(pop,text='2.View employee',command=two,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
    t.Button(pop,text='3.Edit employee details',command=three,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
    t.Button(pop,text='Quit EDMS',fg='Red',bg='white',command=exi,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
    d=t.Button(pop,text="fetch database",command=opndb)
    d.grid(row=4,column=15,padx=25,pady=7)
    pop.mainloop()
    db.mainloop()    
con.close()
root2.mainloop()
