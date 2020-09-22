# Map function:
# It applies a function to all the members of an iteable


crewMate = [
    ("Nami", 4, "Navigator"),
    ("Zoro", 1, "Swordsman"),
    ("Ussop", 2, "Sniper"),
    ("Sanji", 3, "Cook"),
]
# Syntax: map(function, iterable)
x = map(lambda item: (item[0], item[2]), crewMate)
print(x)
job = list(x)
print(job)
