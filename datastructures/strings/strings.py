# Python Program to demonstrate String slicing

# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String1[3:-2])

"""
In Python, Updation or deletion of characters
from a String is not allowed. This will cause
an error because item assignment or item
deletion from a String is not supported.
Although deletion of entire String is possible
with the use of a built-in del keyword.
This is because Strings are immutable, hence
elements of a String cannot be changed once it
has been assigned. Only new strings can be
reassigned to the same name.
"""
