import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

query_table = """
SELECT * FROM users;
"""
for row in cursor.execute(query_table):
	print(row)

cursor.close()
connection.close()
