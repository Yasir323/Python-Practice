# Cost of raising exceptions
from timeit import timeit

code1 = """
def calculate_xfacttor(age):
    if age <= 10:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfacttor(-1)
except ValueError as error:
    pass
    # print(error)
"""
code2 = """
def calculate_xfacttor(age):
    if age <= 10:
        return None
    return 10 / age

xfactor = calculate_xfacttor(-1)
if xfactor == None:
    pass
"""

print("First code: ", timeit(code1, number=10000))
print("Second code: ", timeit(code2, number=10000))
# As we can see, the second code is executed almost 4 times
# faster. Raising an exception is not a good option where speed
# is of utmost important. It makes the code look clean
