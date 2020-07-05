# BINDING NAMES TO OBJECTS

a = "first"
b = "first"
# Returns the actual location where the
# variable is stored
print(id(a))

# Returns the actual location where the
# variable is stored
print(id(b))

# Returns true if both the variables
# are stored in same location
print(a is b)

# Now look at this piece of code
c = [10, 20, 30]
d = [10, 20, 30]
# return the location where the variable
# is stored
print(id(a))

# return the location where the variable
# is stored
print(id(b))

# returns false if the location is not same
print(a is b)
