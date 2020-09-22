import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("json/movies.json").read_text())
#--------------------------------------------------------
# Writing
#--------------------------------------------------------
# with sqlite3.connect("sqlite/db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()
#--------------------------------------------------------
# Reading
#--------------------------------------------------------
with sqlite3.connect("sqlite/db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
