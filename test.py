import sqlite3
conn = sqlite3.connect('mynewsql.db')
cur=conn.cursor()

#cur.execute('CREATE TABLE STUDENT(STD INT,SNAME VARCHAR(20))')

conn.commit()
cur.execute("insert into STUDENT values (1, 'sandy')")
conn.commit()