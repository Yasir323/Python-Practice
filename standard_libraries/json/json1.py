import json
from pathlib import Path


#--------------------------------------------------------
# Writing
#--------------------------------------------------------
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Avengers: Endgame", "year": 2019}
# ]
# data = json.dumps(movies)
# print(data)
# Path("json/movies.json").write_text(data)
#--------------------------------------------------------
# Reading
#--------------------------------------------------------
data = Path("json/movies.json").read_text()
movies = json.loads(data)
for movie in movies:
    print(movie)
