"""
Now there is one problem with our code. If we run:
print(new_func_to_be_decorated.__name__)
# Output: wrap_the_function

That’s not what we expected! Its name is “new_func_to_be_decorated”.
Well, our function was replaced by wrap_the_function.
It overrode the name and docstring of our function.
Luckily, Python provides us a simple function to solve
this problem and that is `functools.wraps`.
"""
from functools import wraps


def func_decorator(decorated_func):
    @wraps(decorated_func)
    def wrap_the_function():
        print("I am being executed before the decorated_func")
        decorated_func()
        print("I am being executed after the decorated_func")
    return wrap_the_function


@func_decorator
def func_to_be_decorated():
    print("I am the function that needs to be decorated.")


func_to_be_decorated()
print("-"*80)
print(func_to_be_decorated.__name__)
"""
Note: @wraps takes a function to be decorated and adds
the functionality of copying over the function name,
docstring, arguments list, etc. This allows us to access
the pre-decorated function’s properties in the decorator.
"""
