# Filter function:
# It applies a function to each member of an iteable and
# if the item matches a specified condition it'll return it.


crewMate = [
    ("Nami", 4, "Navigator"),
    ("Zoro", 1, "Swordsman"),
    ("Ussop", 2, "Sniper"),
    ("Sanji", 3, "Cook"),
    ("Chopper", 5, "Doctor"),
    ("Jimbe", 9, "Helmsman"),
    ("Brook", 8, "Musician"),
    ("Franky", 7, "Shipwright"),
    ("Robin", 6, "Archeologist"),
]
# Syntax: map(function, iterable)
x = filter(lambda item: item[1] < 5, crewMate)
print(x)
east_blue_crew = list(x)
print(east_blue_crew)
