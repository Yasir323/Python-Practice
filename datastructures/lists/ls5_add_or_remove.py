# Addind and removing items to the list
letters = ["a", "b", "c"]
print(letters)


# Add
print("Append")
letters.append("d") # Takes the value as argument
print(letters)

print("Insert")
letters.insert(4, "e")  # First argument: Index, Second argument: Value
print(letters)


# Removing
print("Pop")
letters.pop(4)  # Argument: Index
print(letters)

print("Remove")
letters.remove("d") # Argument: value
# Removes the first occurence of "d"
print(letters)

print("Adding elements back")
letters.append("d")
letters.insert(4, "e")
print(letters)

print("Del")
del letters[3:5]    # Can delete range of values
print(letters)

print("CLear")
letters.clear() # Deletes all the elements
print(letters)
