from getpass import getpass
import random,string
import tkinter as t
import tkinter.messagebox as ms
import mysql.connector as c
u=input('Enter database name: ')
pa=input("Enter password: ")
con=c.connect(host='localhost',user='root',password=f'{pa}',database=f'{u}',autocommit=True)# trouble shoot the executable version
curso=con.cursor()
if con.is_connected():
   print('successfully connected')
else:
   print('not connected')
sql="show tables like 'passwords'"
curso.execute(sql)
dat=curso.fetchone()
chng='jkr'
if dat:
    pass
else:
    ms.showwarning("My SQL Database","no table existes thus creating table ")
    sql="create table passwords(account_name char(200) unique, passwrd char(200) unique);"
    curso.execute(sql)
siz=random.randint(8,16)
p1=['@','#','!','%','^','*','|','blah','ghusuri']
def men(var=1):
    pop=t.Tk()
    def wd1():
        pop.destroy()
        wd()
    def xd1():
        pop.destroy()
        xd()
    def yd1():
        pop.destroy()
        yd()       
    t.Button(pop,text='Create password',command=wd1,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
    t.Button(pop,text='Delete passwords',command=xd1,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
    t.Button(pop,text='Insert passwords',command=yd1,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
    t.Button(pop,text='show passwords',command=zd1,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
    t.Button(pop,text='edit passwords',command=edi,font='Nougat').grid(row=4,column=15,padx=25,pady=7)
    t.Button(pop,text='Quit',command=pop.destroy,font='Nougat').grid(row=5,column=15,padx=25,pady=7)
    if var==2:
        t.Button(pop,text='forgot',command=fgt,font='Nougat').grid(row=6,column=15,padx=25,pady=7)
    pop.mainloop()
def fgt():
    global chng
    ms.showinfo('password manager','Enter the Email address')
    eml=input('--->')
    if eml=='sanjaydas740786@gmail.com':
        chng=input('Enter new password')
    else:
        ms.showwarning('Password manager','Suspicious activity detected!')
        men(var=1)
def zd():
    usr=getpass('Enter the database authentication password: ')
    if usr==chng:
        curso.execute('select * from passwords')
        dat=curso.fetchall()
        if dat:
            for i in dat:
                print(f"{i[0]}:",i[1])
                print("\r")
                print("press enter to continue...",end='')
                kr=input()
                if kr:
                    break
            men()
        else:
            ms.showwarning("Password manager","No passwords exists")
    else:
        ms.showwarning('Password Manager',"Authentication error")
        men(var=2)
def wd():
    global pas,name
    name=input('Enter the account name- ')
    pas=''
    p=string.punctuation
    feed='y'
    while feed=='y' and len(pas)<17:
        #algorithm to generate password
        for i in range(siz):
            if i%2==0:
                pas=pas+random.choice(p)
            a=random.randint(65,119)
            pas=pas+chr(a)
        #end of algorithm
        passql=f"insert into passwords values('{name}','{pas}')"
        print('Password',pas)
        confir=input('ok?\n->')
        if confir=='ok'or confir=='yes' or confir=='y':
            try:
                curso.execute(passql)
                ms.showinfo('Password manager','Successfully created')
                men()
            except Exception as e:
                ms.showwarning('My SQL database',f'warning: {e}')
                pro=input('Do you want to create another password?[y/n/change account name]\n')
                if pro=='change account name':
                    name=input('Enter account name: ')
                    wd()
                if pro=='y':
                    pass
                if pro=='n':
                    men()
                else:
                    pas=''
                    print('Regenerating....\n')
                    wd()
            finally:
                pas=''
        else:
            pas=''
            print('---------------O--------------\n')
            men()
    else:
        con.close()
def xd():
    usr=getpass('Enter the password: ')
    if usr==chng:
        acntnm=input('Enter the account name: ')
        sql=f"delete from passwords where account_name='{acntnm}'"
        curso.execute(sql)
        ms.showinfo('Password manager','Password along with the account deleted')
    else:
        ms.showwarning("Password manager",'Incorrect password')
    men()
def yd():
    try:
        acntnm=input('Enter the account name: ')
        pa=getpass('Enter password for the account: ')
        sql=f"Insert into passwords values('{acntnm}','{pa}')"
        curso.execute(sql)
        ms.showinfo('Password manager','Registered!')
        men()
    except Exception as e:
        ms.showwarning('Password manager',f'{e}')
        men()
pop2=t.Tk()
#-------------------------------------edit password code---------------
def edi():
    usr=input("Enter the account name: ")
    sql=f"Select * from passwords where account_name like '%{usr}%'"
    curso.execute(sql)
    dat=curso.fetchall()
    print(f"Show Account having '{usr}'...\n--------------O-----------")
    if dat:
        j=0
        for i in dat:
            j+=1
            print("%s. %s: %s"%(j,i[0],i[1]))
        usr2=int(input("To select the account to edit password type S.No from the screen: "))
        out=dat[usr2-1]
        print(f"{out[0]}: ",end='')
        chngps=input()
        sql=f"update password set passwrd='{chngps}' where passwrd='{out[1]}'"
        ms.showinfo(title='Password manager',message='Password changed Successfully')
        men()
    else:
       conf= ms.askyesno(title="Password manager",message="No such account exists!\nDo you want to retry?")
       if conf:
           edi()
    #    else:
        #    men()
    

#-------------------------------------edit password code-----------------
def wd1():
    pop2.destroy()
    wd()
def xd1():
    pop2.destroy()
    xd()
def yd1():
    pop2.destroy()
    yd()   
def zd1():
    pop2.destroy()
    zd()
t.Button(pop2,text='Create password',command=wd1,font='Nougat').grid(row=0,column=15,padx=25,pady=7)
t.Button(pop2,text='Delete passwords',command=xd1,font='Nougat').grid(row=1,column=15,padx=25,pady=7)
t.Button(pop2,text='Insert passwords',command=yd1,font='Nougat').grid(row=2,column=15,padx=25,pady=7)
t.Button(pop2,text='show passwords',command=zd1,font='Nougat').grid(row=3,column=15,padx=25,pady=7)
t.Button(pop2,text='edit passwords',command=edi,font='Nougat').grid(row=4,column=15,padx=25,pady=7)
t.Button(pop2,text='Quit',command=pop2.destroy,font='Nougat').grid(row=5,column=15,padx=25,pady=7)
pop2.mainloop()






