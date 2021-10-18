# Function decorators: Decorators let you execute code
# before and after a function.

def func_decorator(decorated_func):

    def wrap_the_function():
        print("I am being executed before the decorated_func")
        decorated_func()
        print("I am being executed after the decorated_func")
    return wrap_the_function


def func_to_be_decorated():
    print("I am the function that needs to be decorated.")


func_to_be_decorated()
print("-"*80)
func_to_be_decorated = func_decorator(func_to_be_decorated)
# Now the 'func_to_be_decorate' is wrapped by the 'wrap_the_function'

func_to_be_decorated()
"""
We just applied the previously learned principles. This
is exactly what the decorators do in Python! They wrap
a function and modify its behaviour in one way or another.
Now you might be wondering why we did not use the @ anywhere
in our code? That is just a short way of making up a
decorated function.
"""
print("+"*80)
@func_decorator
def new_func_to_be_decorated():
    """Hey you! Decorate me!"""
    print("I am very plain and simple.")


new_func_to_be_decorated()
print("*"*80)
# There is one problem with our code
print(new_func_to_be_decorated.__name__)
# The name is wrong.
