# import csv
fh=open("g:\\Submissio report.txt",'w+',newline='')
# csv_reader=csv.writer(fh)
# csv_reader.writerows(['Roll','Name','||','Physics','chem','maths'])
fh.writelines(['Roll    ','Name     ','||       ','Physics      ','chem     ','maths        \n'])
Roll=1
name=input("Enter the name of the student: ")
physics=input("Enter Physics status: ")
chem=input('Enter chem Status: ')
math=input('Enter maths status: ')
loader=[str(Roll),'.      ',name,'        ',physics,'        ',chem,'        ',math,'\n']
# csv_reader.writerows(loader)
fh.writelines(loader)
while name: 
    Roll+=1
    name=input('Enter the name of the student: ')
    if name=='done':
        break
    physics=input("Enter physics status: ")
    chem=input('Enter chem Status: ')
    math=input('Enter the math status: ')
    loader=[str(Roll),'.      ',name,'        ',physics,'        ',chem,'        ',math,'\n']
    # csv_reader.writerows(loader)
    fh.writelines(loader)
fh.close()
print("viewing tables....\n\n")         
with open('g:\\Submissio report.txt','r',newline='') as h:
    # viewr=csv.reader(h)
    for i in h:
        # a=str(i[::])
        print(i,end='')