'''
The reduce() function in Python takes in a function
and a list as argument. The function is called with
a lambda function and a list and a new reduced result
is returned. This performs a repetitive operation over
the pairs of the list.
'''
# Program to get a sum of a list
from functools import reduce
li = [234, 3, 435, 4567, 5687, 6876, 86, 8, 76, 55, 4]
sum = reduce((lambda x, y: x + y), li)
print(sum)
