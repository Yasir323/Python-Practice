# Generators declaration is similar to a list comprehension
# But instead of a square brackets we have parenthesis
# They are used in place of list when we have a huge list.
# Generator objects are iterable and in each iteration
# they generate a new value so it only takes up a space as
# much as one element of a list.
from sys import getsizeof

square = (x ** 2 for x in range(5))
print(square)
for x in square:
    print(x)

print("Let's see the advantage of using a generator:")
odd_list = [x for x in range(10000000) if x %2 == 1]
odd_gen = (x for x in range(10000000) if x %2 == 1)
print("Size of list is: ", getsizeof(odd_list))
print("Size of generator is: ", getsizeof(odd_gen))

print("If we increase the size list and generators then")
print("the memory taken by list will increase but")
print("for generatorit remains the same.")
