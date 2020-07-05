'''
Packing:
When we don’t know how many arguments need to be passed
to a python function, we can use Packing to pack all
arguments in a tuple.
'''
# A Python program to demonstrate use of packing
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
