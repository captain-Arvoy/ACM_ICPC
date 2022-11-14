import csv
fh=open("g:\\Submissio report.csv",'w+',newline='')
csv_reader=csv.writer(fh)
csv_reader.writerows(['Roll','Name','||','Physics','chem','maths'])
Roll=1
name=input("Enter the name of the student: ")
physics=input("Enter Physics status: ")
chem=input('Enter chem Status: ')
math=input('Enter maths status: ')
loader=[str(Roll),'.',name,physics,chem,math]
csv_reader.writerows(loader)
while name: 
    Roll+=1
    name=input('Enter the name of the student: ')
    if name=='done':
        break
    physics=input("Enter physics status: ")
    chem=input('Enter chem Status: ')
    math=input('Enter the math status: ')
    loader=[str(Roll),name,physics,chem,math]
    csv_reader.writerows(loader)
fh.close()
print("viewing tables....\n\n")         
with open('Submissio report.csv','r',newline='') as h:
    viewr=csv.reader(h)
    for i in viewr:#error aa raha hai "io.UnsupportedOperation: not readable"
        a=str(i[::])
        print(a,end='')