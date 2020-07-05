'''
Unpackimg:
Consider a situation where we have a function that receives
four arguments. We want to make call to this function and we
have a list of size 4 with us that has all arguments for the
function. If we simply pass list to the function, the call
doesn’t work. We can use * to unpack the list so that all
elements of it can be passed as different parameters.
** is used for dictionaries
'''
# A sample function that takes 4 arguments and prints them
def fun(a, b, c, d):
    print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)
d = {'a':2, 'b':4, 'c':10, 'd': 20}
fun(**d)
