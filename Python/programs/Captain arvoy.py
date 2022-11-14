import time
import random
import mysql.connector as mc
con=mc.connect(host='localhost',user='root',passwd='',database='test')
curso=con.cursor()
sql="drop table if exists book_details"
curso.execute(sql)
sql="create table if not exists book_details(Book_no integer(6) primary key,Book_title varchar(180),price integer(6),commission integer(3),publication_name char(50))"

curso.execute(sql)
num=1
i=1
for i in range(1,11):
   # bkt1=input("Input the book name:")
   bkt=["python","# Challenge","import txt.py","Economics","Greek","caitanya caritamirt","srimad Bhagvatam","Bhakti rasamrit sindhu","Bhagvad gita","Calculus","geometery"]
   prc=int(random.randint(2, 6000))
   cms=int(random.randint(0, 101))
   # pbsnm=input("Enter the publisher name:")
   var=("Rabi","Macmillian","Vedavyas","Kaviraj goswami","ISKCON","Arihant")
   pbsnm=random.choice(list(var))
   sql="insert into book_details values({},'{}',{},{},'{}')".format(i,bkt[i],prc,cms,pbsnm)
   curso.execute(sql)
   con.commit()
   print("%s Generated"%i)
sql="select distinct(publication_name) from book_details"
curso.execute(sql)
dat=curso.fetchall()
#1. & 2.
for i in range(len(dat)):
   print(f"---------\n{i+1}.",dat[i][0])

print("\n")
for i in range(4):
   sql=f"select count(Book_title) from book_details where publication_name='{dat[i][0]}'"
   curso.execute(sql)
   dat2=curso.fetchall()
   print(f"Number of books by {dat[i][0]}={dat2[0][0]}")
# 3.
sql="select sum(commission) from book_details"
curso.execute(sql)
dat=curso.fetchall()
print("commission=",dat[0][0],"%")
# 4.
sql="select sum(price) from book_details"
curso.execute(sql)
dat=curso.fetchall()
for i in dat:
   print(f"Total cost of all books=Rs.{dat[0][0]}")
   
   
   
