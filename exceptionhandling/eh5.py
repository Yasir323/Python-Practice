# Raising exceptions
def calculate_xfacttor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


# https://docs.python.org/3/library/exceptions.html
try:
    calculate_xfacttor(-1)
except ValueError as error:
    print(error)
# We can also define our own exceptions.
