# DOING THINGS TO LISTS

# This is not a list, technically
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

# Now it is
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # Fisrt element
print(stuff[-1]) # Last element
print(stuff.pop()) # Last element, pointer is still there
print(' '.join(stuff)) # Join the elements as in ten_things
print('#'.join(stuff[3:5]))
