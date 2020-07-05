'''
The map() function in Python takes in a function
and a list as argument. The function is called
with a lambda function and a list and a new list
is returned which contains all the lambda modified
items returned by that function for each item.
'''
# Program to get double of a list
li = [4, 453,5, 54, 45, 45, 45, 67, 78, 78, 87, 23]
double = list(map(lambda x: (x * 2), li))
print(double)
