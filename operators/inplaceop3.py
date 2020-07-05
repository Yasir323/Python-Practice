# Python code to demonstrate the working of
# ixor(), ipow(), ior(), iand(), ilshift() and irshift()

# importing operator to handle operator operations
import operator

# using ixor() to exclusive or and assign value
x = operator.ixor(10,5);

# printing the modified value
print ("The value after xoring and assigning : ",end="")
print (x)

# using ipow() to exponentiate and assign value
x = operator.ipow(5,4);

# printing the modified value
print ("The value after exponentiating and assigning : ",end="")
print (x)


# using ior() to or, and assign value
x = operator.ior(10,5);

# printing the modified value
print ("The value after bitwise or, and assigning : ",end="")
print (x)

# using iand() to and, and assign value
x = operator.iand(5,4);

# printing the modified value
print ("The value after bitwise and, and assigning : ",end="")
print (x)


# using ilshift() to bitwise left shift and assign value
x = operator.ilshift(8,2)
# 8 = 1000, lshist by 2 places -> 100000 = 32

# printing the modified value
print ("The value after bitwise left shift and assigning : ",end="")
print (x)

# using irshift() to bitwise right shift and assign value
x = operator.irshift(8,2);

# printing the modified value
print ("The value after bitwise right shift and assigning : ",end="")
print (x)
