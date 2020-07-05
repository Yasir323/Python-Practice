
# Python code to demonstrate working of
# concat() and contains()

# importing operator module
import operator

# Initializing string 1
s1 = "geeksfor"

# Initializing string 2
s2 = "geeks"

# using concat() to concatenate two strings
print ("The concatenated string is : ",end="")
print (operator.concat(s1,s2))

# using contains() to check if s1 contains s2
if (operator.contains(s1,s2)):
       print ("geeksfor contains geeks")
else : print ("geeksfor does not contain geeks")
