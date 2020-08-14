# Introduction
try:
    age = int(input("Age: "))
except ValueError:
    # Now if user enters anything but an integer
    # the program will not crash giving a ValueError
    # instead the following messgae will be printed
    # and the program execution will be completed.
    print("You did not enter a valid age.")
# If we didn't use error handling the program
# would've crashed and the following line wouldn't run.
print("Execution continues.")
