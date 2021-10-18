# Passing function to a function

def hi(name="Yasir"):
    return "Hi, " + name

# Passing a functon to a function
# print(hi())

# Assign a function to a variable
greet = hi
# print(greet())

# We can even delete a function
del hi
# print(hi())
# Output-NameError: name 'hi' is not defined
print(greet())
