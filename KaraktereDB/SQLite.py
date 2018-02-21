import sqlite3
conn = sqlite3.connect("grades.db")
c = conn.cursor()


c.execute("CREATE TABLE STUDENT (studentKey INTEGER, name TEXT)")
c.execute("CREATE TABLE FAG (fagKey INTEGER, name TEXT)")
c.execute("CREATE TABLE GRADE (studentKey INTEGER, fagKey INTEGER, grade INTEGER)")
