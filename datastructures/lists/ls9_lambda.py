# SORTING COMPOSITE LIST USING LAMBDA

crewMate = [
    ("Nami", 4),
    ("Zoro", 1),
    ("Ussop", 2),
    ("Sanji", 3),
]

crewMate.sort(key=lambda item: item[1])

print(crewMate)
