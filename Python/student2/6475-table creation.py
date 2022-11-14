def table_creation_railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table railway(name varchar(100),phno varchar(15)  primary key,age int(4),gender varchar(50),from_f varchar(100),to_t varchar(100),date_d varchar(20))"
    cursor.execute(s1)
    print("Table railway created!")
table_creation_railway()




def table_creation_user_accounts():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s2="create table user_accounts(fname varchar(100),lname varchar(100),user_name varchar(100) ,password varchar(100) primary key, phno varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
    cursor.execute(s2)
    print("Table user_accounts created!")
table_creation_user_accounts()

