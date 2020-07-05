'''
In Python, anonymous function means that a
function is without a name. the lambda keyword
is used to create anonymous functions.
It has the following syntax:
lambda arguments: expression

This function can have any number of arguments
but only one expression, which is evaluated and returned.
'''
# PROGRAM TO ILLUSTRATE DIFFERENCE BETWEEN def() & lambda
def cube(y):
    return y*y*y

g = lambda x: x*x*x

print(cube(2))
print(g(3))
