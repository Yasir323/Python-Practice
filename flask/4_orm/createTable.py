import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS users 
(id INTEGER PRIMARY KEY, username TEXT, password TEXT);
"""
cursor.execute(create_table)

create_table = """
CREATE TABLE IF NOT EXISTS items 
(id INTEGER PRIMARY KEY, name TEXT, price REAL);
"""
cursor.execute(create_table)

# user = (1, 'Yasir', '123')
# insert_user = """
# INSERT INTO users (id, username, password)
# VALUES (?, ?, ?);
# """
# cursor.execute(insert_user, user)

# connection.commit()

# users = [
# 	(2, 'Luffy', 'meat'),
# 	(3, 'Sanji', 'ladies'),
# 	(4, 'Zoro', 'sake')
# ]
# cursor.executemany(insert_user, users)

connection.commit()

cursor.close()
connection.close()
