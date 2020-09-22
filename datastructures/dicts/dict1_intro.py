# Declaration
point = {"x": 1, "y": 2}
# OR
point2 = dict(x=3, y=4)

# Changing values
point["x"] = 3

# Searching
if "x" in point:
    print(point["x"])
# OR
print(point.get("z"))
# get() method takes a second parameter which is the default value
# to be printed if the key is not found

# Deleting
point["z"] = 5
print(point)
del point["z"]
print(point)


# Looping over dictionary
point["z"] = 5
print("Looping over a list")
for key in point:
    print(key, point[key])
# OR using items() method
print("USing items() method:")
for key, value in point.items():
    print(key, value)
