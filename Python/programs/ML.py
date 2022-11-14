'''priority of computer is to draw or win the match'''
import tkinter.messagebox
import random
import mysql.connector as c
con=c.connect(host='localhost',user='root',password='',database='Machine_learning')
if con.is_connected():
   print('successfully connected')
else:
   print('not connected')
curso=con.cursor()
sql="Select * from oldgames"
curso.execute(sql)
data=curso.fetchall()
human_score,computer_score=0,0
rul_buk={'/':1,'*':2,'-':3}
round=0;
stone_pap=['/','*','-']
event2={'/':1.0,'*':1.0,'-':1.0}
event={'/':data[0][1],'*':data[1][1],'-':data[2][1]}
decision={'/':0.0,'*':0.0,'-':0.0}
event_weight=0;
weights2={'/':0.333,'*':0.333,'-':0.333};
weights={'/':data[0][2],'*':data[1][2],'-':data[2][2]};
def decs():
    denominator=weights['/']*(event['/']/weights['/']) + weights['*']*(event['*']/weights['*']) + weights['-']*(event['-']/weights['-'])
    for i in weights:
        P_hypo=weights[i]
        decision[i]+=(P_hypo*(event[i]/P_hypo))/denominator;
    if decision['*']==decision['-']==decision['/']:
        return random.choice(stone_pap)
    if decision['/']>decision['*']:
        if decision['/']>decision['-']:
            return '/'
        else:
            return '-'    
    elif decision['*']>decision['-']:
        return '*'
    else:
        return '-'    
database=input("do you want to reset data?(y/n): ")
if database=='y':
    for i in event:
        sql=f"update oldgames set evidence=1.0,hypothesis=0.333 where sign='{i}' "
        curso.execute(sql)
        con.commit()
        
def rand(human_choice):
    weights[human_choice]+=0.01;
    for i in weights:
        if i !=human_choice:
            weights[i]-=0.005
    return decs()
continu='y'
no_of_rounds=int(input('Enter the number of rounds: '))
while continu=='y':
    round+=1;
    event_weight=1/round;
    human=input("Enter Stone(/) paper(*) scissor(-):\n");
    # human=random.choice(['/','*','-'])
    comput=rand(human) #rand will be our bayesian function
    if (human!='*' and comput!='/') or (human!='/' and comput!='*'):
        rul_buk={'/':1,'*':2,'-':3}
    elif (human!='*' and comput!='-') or (human!='-' and comput!='*'):
        rul_buk={'/':2,'*':3,'-':1}
    if (human!='*' and comput!='-') or (human!='-' and comput!='*'):
        rul_buk={'/':3,'*':2,'-':1}

    #stone paper ka logic galat hai
    for i in event:
        if i==human:
            weights[i]+=event_weight
        else:
            weights[i]-=event_weight
    if human!=comput:
        if rul_buk[human]>rul_buk[comput]:
            #human wins
            human_score+=1
            print('computer: %s vs You: %s'%(comput,human))
            print("You won!")
            event[human]+=event_weight
            pass
        else:
            #computer wins
            computer_score+=1
            print('computer: %s vs You: %s'%(comput,human))
            print("I won!")
            event[human]-=event_weight
            pass
    else:
        print('computer: %s vs You: %s'%(comput,human))
        print("Oh Draw ho gaya ;p")
        pass
        #computer wins as it is draw but p(player choosing that choice decreases)
    # continu=input("Lets play again(y/n): ")
    if round>=no_of_rounds:
        a=tkinter.messagebox.askyesno("Machine","Do you want to play again?")
        if a:
            continu='y'
        else:
            continu='n'
else:
    for i in event:
        sql=f"update oldgames set evidence={event[i]},hypothesis={weights[i]} where sign='{i}' "
        curso.execute(sql)
        con.commit()
    con.close()
    print(f"\n\ncomputer score={computer_score}\nYour score={human_score}\ntotal rounds={round}");