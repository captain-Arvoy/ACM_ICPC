def Create_Database_Railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='')    
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="Drop database if exists railway"
    cursor.execute(s1)
    s2="create database railway"
    cursor.execute(s2)
    print("Database created!")
Create_Database_Railway()
