import sqlite3

conn = sqlite3.connect('testDB.db')
conn1 = sqlite3.connect('DB1.db')

print("connect success")

c = conn.cursor()

# create table 
query_create = """
	       CREATE TABLE IF NOT EXISTS USER ( 
                    EMAIL VARCHAR PRIMARY KEY,
                    USERNAME VARCHAR,
	                PASSWORD VARCHAR
               );
	       """

c.execute(query_create)
print("Table Create Successfully!")

# insert table
query_insert = """
               insert into user (email, username, password)
               values ('123@gmail.com', '123', '123');
	       """
# c.execute(query_insert)
print("Insert successfully!")
# conn.commit()


# select table
query_select = """
               SELECT * FROM user;
               """
res = c.execute(query_select)
# print(res.len)
# print(len(res))

for row in res:
   print(row)
   print(row[0])
   print(row[1])
   print(row[2])

userlist = res.fetchall()
print(userlist)
print("user count is ", len(userlist))
# print(userlist[0])
# print(userlist[0][0])


conn.close()
