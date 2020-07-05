# PROGRAM TO TAKE MULTIPLE INPUTS
# FROM THE USER


# SPLIT METHOD
"""This function helps in getting a multiple inputs from user . It breaks the given input by the specified separator. If separator is not provided then any white space is a separator. Generally, user use a split() method to split a Python string but one can used it in taking multiple input.
Important: While giving input user must press 'space' key between different values."""

a, b, c = input("Enter three values: ").split()
print("First number is ", a)
print("Second number is {}".format(b))
print(f"Third number is {c}")

# LIST COMPREHENSION METHOD
"""List comprehension is an elegant way to define and create list in Python. We can create lists just like mathematical statements in one line only. It is also used in getting multiple inputs from a user."""

x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First number is ", x)
print("Second number is {}".format(y))
print(f"Third number is {z}")
