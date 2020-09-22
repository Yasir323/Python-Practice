# SORTING COMPOSITE LIST

crewMate = [
    ("Nami", 4),
    ("Zoro", 1),
    ("Ussop", 2),
    ("Sanji", 3),
]

# Now if we try to sort this composite list,
# Nothing will happen.

crewMate.sort()
print(crewMate)

def sort_list(crewMate):
    return crewMate[1]


crewMate.sort(key=sort_list)
# Note: We're not calling the function itself,
# we're just passing the reference to the function
print(crewMate)
