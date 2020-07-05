'''
A programming language is said to support first-class
functions if it treats functions as first-class objects.
Python supports the concept of First Class functions.

Properties of fisrt class functions:
1. A function is an instance of the object type.
2. You can store the function in a variable.
3. You can pass the function as a parameter to another function.
4. You can return the function from another function.
5. You can store them in a DS such as hash tables, lists, etc.
'''

# PROGRAM TO ILLUSTRATE THAT FUNCTIONS CAN BE TREATED AS OBJECTS.
def shout(text):
    return text.upper()

print(shout('Hello'))
# Pay attention to the following line.
yell = shout
print(yell('Hello'))
