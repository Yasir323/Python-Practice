# Inplace operators


# Python code to demonstrate difference between
# Inplace and Normal operators in Immutable Targets

# importing operator to handle operator operations
import operator

# Initializing values
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
c = operator.add(a,b)

# using iadd() to add the arguments passed
z = operator.iadd(x,y)

# printing the modified value
print ("Value after adding using normal operator : ",end="")
print (c)

# printing the modified value
print ("Value after adding using Inplace operator : ",end="")
print (z)

# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ",end="")
print (a)

# printing value of first argument
# value is unchanged
print ("Value of first argument using Inplace operator : ",end="")
print (x)

# Mutable objects
d = [1, 2, 4, 5]
e = operator.add(d,[1, 2, 3])
print ("Value after adding using normal operator : ",end="")
print (e)
print ("Value of first argument using normal operator : ",end="")
print (d)

w = operator.iadd(d,[1, 2, 3])
print ("Value after adding using Inplace operator : ",end="")
print (w)
print ("Value of first argument using Inplace operator : ",end="")
print (d)
