# Returning functions from within functions

def hi(name="yasir"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasir":
        return greet
    else:
        return welcome

"""
Just take a look at the code again. In the if/else
clause we are returning greet and welcome, not greet()
and welcome(). Why is that? It’s because when you put
a pair of parentheses after it, the function gets executed;
whereas if you don’t put parenthesis after it, then it
can be passed around and can be assigned to other
variables without executing it.
"""
a = hi()
# print(a)
print(a())

