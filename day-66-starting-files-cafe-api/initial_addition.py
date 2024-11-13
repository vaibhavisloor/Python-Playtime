import sqlite3

connection = sqlite3.connect("instance/cafes.db")

cursor = connection.cursor()


# cursor.execute('''CREATE TABLE IF NOT EXISTS cafes(
#                id INTEGER PRIMARY KEY,
#                name VARCHAR(50) NOT NULL,
#                location VARCHAR(50) NOT NULL
#                )''')

# cafes = [
#     ('Cafe Mocha', 'Downtown'),
#     ('Latte Land', 'Uptown'),
#     ('Brew Heaven', 'City Center')
# ]

# for cafe in cafes:
#     cursor.execute('''INSERT INTO cafes (name,location) VALUES (?,?)''',cafe)

# import random
# cursor.execute("select id from cafes order by id desc limit 1")
# id = cursor.fetchone()
# max_id = id[0]

# random_id = random.randint(1,max_id)

# # cursor.execute('select * from cafes where id = ?',(random_id,))
# # rows = cursor.fetchmany()
# # print(rows)
# # print(type(rows[0]))


# cursor.execute("select * from cafes where id = 10")
# row = cursor.fetchmany()
# print(row)
# connection.commit()

cursor.execute("select * from cafes")
row = cursor.fetchall()
print(row)