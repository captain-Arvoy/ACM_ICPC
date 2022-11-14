import random
from tkinter.messagebox import askyesno, showinfo, showwarning
import mysql.connector as c
import tkinter as t
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
            
            showinfo('database connector','Successfully connected')
            
        curso=con.cursor()
        sql='drop table if exists employee;'
        curso.execute(sql)
        sql="Create table employee(S_no integer(5) primary key,name varchar(75),age integer,gender char(75),designation varchar(70),salary integer(75));"
        curso.execute(sql)
    except:
        showwarning('Database connetor','   Invalid credentials   ')
        retry()

choice=1
def main():
    while choice:
        def opndb():
            curso.execute('select * from employee')
            datc=curso.fetchall()
            if datc:
                db=t.Tk()
                db.wm_withdraw()
                db.wm_deiconify()
                db.title('database')
                db.geometry("600x400")
                db.wm_deiconify()
                d.grid_forget()
                curso.execute('select * from employee')
                dat=curso.fetchall()
                rw=1
                if dat:
                    for i in dat:
                        txt=f"{rw}.{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}"
                        t.Label(db,text=txt).grid(row=rw,column=0,padx=15,pady=3)
                        rw+=1
                db.mainloop()    
            else:
                showwarning("EDMS","Empty Database")
        pop=t.Tk()
        def exi():
            pop.destroy()
            showinfo('Devolopers message','Thank you for choosing EDMS, Give us Full marks! XD')
            global choice
            choice=False
            main()
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
    con.close()

print('Welcome....To EDMS(Employee data  management system)....\nplease enter your database credentials')
for i in range(2000**2+30000):
    pass
hst=input('Enter host name: ')
usr=input('Enter the user name: ')
passe=input('Enter the password: ')
db=input('Enter the database: ')
try:
    con=c.connect(host=f'{hst}',user=f'{usr}',password=f'{passe}',database=f'{db}',autocommit=True)
    if con.is_connected:
        showinfo('Database connector','Connection established successfully')
except:
    
    showwarning('Database connetivity error','Invalid credentials')
    
    retry()
con=c.connect(host=f'{hst}',user=f'{usr}',password=f'{passe}',database=f'{db}',autocommit=True)
curso=con.cursor()
sql='drop table if exists employee;'
curso.execute(sql)
sql="Create table employee(S_no integer(5) primary key,name varchar(75),age integer,gender char(75),designation varchar(70),salary integer(75));"
curso.execute(sql)
sn=0
accc=0
def edm():
    global sn,accc
    inp=''
    while inp!='dn':
        sn+=1
        accc+=1
        if accc%4==0:      
            showinfo('Database manager','If you want to exit then type "quit" or "exit" in the name field')
        try:
             nam=input('Enter the name of the employee:')
             if nam.lower()=='quit' or nam.lower()=='exit':
                 return None
             age=int(input('Enter the age of the person:'))
             gen=input('Enter the gender of the person:')
             gen3='classified'
             if gen.lower()=='male' or gen.lower()=='m':
                 gen3='M'
             elif gen.lower()=='female' or gen.lower()=='f':
                 gen3='F'
             desegn=input('Enter the designation of the employee:')
             desegn=desegn.capitalize()
             sal=int(input('Enter the salary of the employee:'))
             sql3=f"insert into employee values({sn},'{nam}',{age},'{gen},{gen3}','{desegn}',{sal});"
             curso.execute(sql3)
             print("---------------inserted------------")
        except Exception as e:
             showwarning('Input error',f'{e}')
             print("------cancelling entry-------")

#-----------------Table created------------------------------------------------------------------------------------------------------
wish=input('Do you want to create machine generated \'employee\' table:\n')
if wish=='yo'or wish=='yes' or wish=='y' or wish=='[y]' or wish=='yep':
    nam1=['Yashoda','Dhruv','Abhay']
    midnm=['nandan','vishnu','Aditya']
    las=['dasa','Roshan','kishor']
    i=0
# lalala lori dudh ki katori dudh mein batasha......mamma ne mujhe data 
    gen=['M','F']
    desgn=['Team coordinator','CEO','Product supervisor','Programmer','Trainer','script writer','Reporter','support','legal advisor','travel agent']
    while i<30:
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
            print(f'loading {i//3*10}%',end='\r')
else:
    pass

#--------------------------database created----------------------------------------------------------------------------------------------------------------------------------------      
def newemployee():
    user=input('\rEnter your username for database access: ')
    if user=='I':
        user='admin21'
        passw='15987'
    else:
        passw=input('Enter pin: ')
    if user=='admin21' and passw=='15987':
        print('Authentication verified')
    else:
        
        showwarning('Authentication error','INCORRECT USER OR PASSWORD DETAILS')
        print('----------------X-------------')
        newemployee()
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
            curso.execute(sql3)
            print("-------inserted--------")
       except Exception as e:
            showwarning('Input error',f'{e}')
            print("------cancelling entry-------")
            if i<siz:
                continue
    main()
def all():
    sql="select * from employee"
    curso.execute(sql)
    data=curso.fetchall()
    if data:
        for i in data:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")
    else:
        showwarning("Database manager","No data available")
def employeeview():
    #check
    sqlc="select * from employee"
    curso.execute(sqlc)
    datc=curso.fetchall()
    if datc:
        user=input('\rEnter your username for database access: ')
        if user=='I':
            user='admin21'
            passw='15987'
        else:
            passw=input('Enter pin: ')
        if user=='admin21' and passw=='15987':
            print('Authentication verified...\n ')
        else:

            showwarning('Authentication error','INCORRECT USER OR PASSWORD DETAILS')

            print("reloading....")

            employeeview()
        pref=input('By which parameters you  want to view:\n1.name \n2.gender \n3.designation \n4.salary\n\r5.Show all employee details(Type \'5\' for this option)\n\r(Enter just option name)\n\r')
        if pref=='5':
            all()
            main()
        if pref=='name' or pref=='1':
            usein=input('Enter the username: ')
            pref="name"
            data=f"select * from employee where {pref}='{usein}'"
        elif pref=='salary' or pref=='4':
            print("Enter the range of salary:-\t[Example-\"45000 52000]\"")
            rang=input().split()
            rnge=list(map(int,rang))
            data=f"select * from employee where salary between {rnge[0]} and {rnge[1]}"
        else:
            usein=input(f'Enter the {pref} of the employee you want to see: ')
            data=f"select * from employee where {pref}='{usein}'"
        curso.execute(data)
        dat=curso.fetchall()
        if dat:
            for i in dat:
                print(i)
        else:

            showwarning('database exception','No employee by this name exists in database')
        main()
    else:
        showwarning("EDMS","Empty Database")
        

def employee_editor():
    sqlc="select * from employee"
    curso.execute(sqlc)
    datc=curso.fetchall()
    if datc:
        user=input('\rEnter your username for database access: ')
        if user=='I':
            user='admin21'
            passw='15987'
        else:
            passw=input('Enter pin: ')
        if user=='admin21' and passw=='15987':
            print('Authentication verified')
        else:
            
            showwarning('Authentication error','INCORRECT USER OR PASSWORD DETAILS')
            
            print("---------------X---------------\n")
            employee_editor()
        prin=t.Tk()
        prin.wm_withdraw()
        def retr():
            dat=[]
            par=input('\rHow you want to search by:\n1.name\n2.by gender\n3.by designation\n4.by salary\n(Enter the name of the name of the option)\n')
            if par=='salary' or par=='4':
                rng=t.Tk()
                def gtrng():
                    global a2,b2,mx1,mn1
                    mx1=t.StringVar(rng)
                    mn1=t.StringVar(rng)
                    rng.title('Salary info. ')
                    a=t.Label(rng,text='Max salary of employee: ')
                    a.grid(row=4,column=0)
                    a2=t.Entry(rng,textvariable=mx1)
                    a2.grid(row=4,column=1)
                    b=t.Label(rng,text='Min salary of the employee: ')
                    b.grid(row=3,column=0)
                    b2=t.Entry(rng,textvariable=mn1)
                    b2.grid(row=3,column=1)            
                    sub=t.Button(rng,text='Enter',bg='blue',fg='white',command=dest)
                    sub.grid(row=6,column=6)
                def dest():
                    rng.destroy()
                    global dat
                    mn=mn1.get()
                    mx=mx1.get()
                    sql=f"select * from employee where salary between {mn} and {mx}"
                    showinfo('salary info.','Details submitted successfully')
                    curso.execute(sql)
                    dat=curso.fetchall()
                    ac=1
                    if dat:
                        for i in dat:
                            print(f"{ac}.{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")
                            ac+=1
                    else:
                        showwarning('Data error','No employee found')
                        main()
                    e_inf=input('Which info you want to change?\n')
                    e_inf_no=int(input('Which number employee you want to change?\n '))
                    cng=askyesno(title='Data transmission control',message=f'you want to change {e_inf} of {e_inf_no}th employee on the screen')
                    if cng:
                        fecher = dat[e_inf_no-1][1]
                        pull=f"select {e_inf} from employee where name='{fecher}'"
                        curso.execute(pull)
                        curso.fetchall()
                        grp=['name',"gender","designation"]
                        upd=input(f"Enter the {e_inf} to update: ")
                        if e_inf in grp:
                            sqls=f"Update employee set {e_inf}='{upd}' where name='{fecher}'"
                            print(sqls)
                            curso.execute(sqls)
                            showinfo("Data manager","Changed successfully!")
                        else:
                            sqls=f"Update employee set {e_inf}={upd} where name='{fecher}'"
                            curso.execute(sqls)
                            showinfo("Data manager","Changed successfully!")
                        main()
                    else:  
                        retr()
                gtrng()
                rng.mainloop()
            else:
                empnm=input(f'Enter the {par} of the employee: ')
                try:
                    emp=int(empnm)
                    sql=f"Select * from employee where {par}='{emp}'"
                    curso.execute(sql)
                    dat=curso.fetchall()
                except:
                    empnm=empnm.upper()
                    sql=f"Select * from employee where {par}='{empnm}'"
                    curso.execute(sql)
                    dat=curso.fetchall()
            if dat:
                ac=1
                if dat:
                   for i in dat:
                       print(f"{ac}.{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")
                       ac+=1
            else:
                showwarning('Data error','No employee found')
                retr()
            return dat
        datc=retr()
        e_inf=input('Which info you want to change?\n')
        e_inf_no=int(input('Which number employee you want to change?\n '))
        cng=askyesno(title='Data transmission control',message=f'Do you confirm to change {e_inf} of {e_inf_no}th employee on the screen')
        if cng:
            fecher = datc[e_inf_no-1][1]
            grp=['name',"gender","designation"]
            upd=input(f"Enter the {e_inf} to update: ").upper()
            if e_inf in grp:
                sqlse=f"Update employee set {e_inf}='{upd}' where name='{fecher}'"
                print(sqlse)
                curso.execute(sqlse)
                showinfo("Data manager","Changed successfully!")
                main()
            else:
                sqlse=f"Update employee set {e_inf}={upd} where name='{fecher}'"
                curso.execute(sqlse)
                showinfo("Data manager","Changed successfully!")
                main()
        else:
            retr()
    else:
        showwarning("EDMS","Empty database")
    main()


    
#main
choice=1
while choice:
    def opndb():
        db2=t.Tk()
        db2.wm_withdraw()
        db2.wm_deiconify()
        db2.title('database')
        db2.geometry("600x400")
        db2.wm_deiconify()
        d.grid_forget()
        curso.execute('select * from employee')
        dat=curso.fetchall()
        rw=0
        if dat:
            for i in dat:
                i1=i
                t.Label(db2,text=f'{i1}').grid(row=rw,column=0,padx=15,pady=3)
                rw+=1
        db2.mainloop()    
#X_X meri band baj gayi hai.....aur nahi ho sakta kal se JEE meri Jaan
    pop2=t.Tk()
    def exi():
        pop2.destroy()
        showinfo('Devolopers message','Thank you for choosing EDMS, Give us Full marks! XD')
        global choice
        choice=False
        main()
    def one():
        pop2.destroy()
        newemployee()
    def two():
        pop2.destroy()
        employeeview()
    def three():
        pop2.destroy()
        employee_editor()
    t.Label(pop2,text='Click your choice',fg='red',font='Nougat').grid(row=5,column=15,padx=25,pady=7)
    t.Button(pop2,text='1.Register employee',command=one,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
    t.Button(pop2,text='2.View employee',command=two,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
    t.Button(pop2,text='3.Edit employee details',command=three,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
    t.Button(pop2,text='Quit EDMS',fg='Red',bg='white',command=exi,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
    d=t.Button(pop2,text="fetch database",command=opndb)
    d.grid(row=4,column=15,padx=25,pady=7)
    pop2.mainloop()
con.close()
