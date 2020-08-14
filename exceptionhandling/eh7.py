# Program to depict Raising Exception

try:
    raise NameError("Error called.")  # Raise Error
except NameError as error:
    print("An exception\n")
    print(error)
    raise  # To determine whether the exception was raised or not
