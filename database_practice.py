import mysql.connector as connector
# connection = connector.connect(host='localhost', user='root', password='')

# # create database
# query = 'CREATE DATABASE mydb'
# cursor = connection.cursor()
# cursor.execute(query)
# connection.commit()
# connection.close()

# create table
# connection = connector.connect(host='localhost', user='root', password='', database='mydb')
# q = 'create table student(id int primary key, name varchar(255))'
# cursor = connection.cursor()
# cursor.execute(q)
# connection.commit()
# print('table successfully created')
# connection.close()

# insert records
# connection = connector.connect(host='localhost', user='root', password='', database='mydb')
# q = 'insert into student values(2, \'abc\')'
# cursor = connection.cursor()
# cursor.execute(q)
# connection.commit()
# print('value successfully inserted')
# q = 'insert into student values(3, \'pqr\')'
# cursor = connection.cursor()
# cursor.execute(q)
# connection.commit()
# print('value successfully inserted')
# connection.close()

# print all records
connection = connector.connect(host='localhost', user='root', password='', database='mydb')

q = 'select * from student'
cursor = connection.cursor()
cursor.execute(q)
res = cursor.fetchall()

for ID,name in res:
    print(ID, name)

connection.close()