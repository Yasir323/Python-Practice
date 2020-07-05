
# Python code to demonstrate working of
# and_(), or_(), xor(), invert()

# importing operator module
import operator

# Initializing a and b

a = 1

b = 0

# using and_() to display bitwise and operation
print ("The bitwise and of a and b is : ",end="")
print (operator.and_(a,b))

# using or_() to display bitwise or operation
print ("The bitwise or of a and b is : ",end="")
print (operator.or_(a,b))

# using xor() to display bitwise exclusive or operation
print ("The bitwise xor of a and b is : ",end="")
print (operator.xor(a,b))

# using invert() to invert value of a
operator.invert(a)

# printing modified value
print ("The inverted value of a is : ",end="")
print (a)
