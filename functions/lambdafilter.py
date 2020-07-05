'''
The filter() function in Python takes in a function
and a list as arguments. This offers an elegant way
to filter out all the elements of a sequence “sequence”,
for which the function returns True.
'''
# Program to return odd numbers from a list
li = [5, 7, 23, 432, 345, 345, 567, 657, 23, 34, 78, 76]
odd = list(filter(lambda x: (x % 2 != 0), li))
print(odd)
