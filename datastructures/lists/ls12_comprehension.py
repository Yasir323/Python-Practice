# LIST COMPREHENSION

# Creating a LIST
# Syntax: [variable iteration expression]
odd = [x for x in range(20) if x % 2 != 0]
print(odd)

# Mapping and filtering
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

east_blue_crew = [item for item in crewMate if item[1] < 5]
print(east_blue_crew)
