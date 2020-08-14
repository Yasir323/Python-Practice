# Handling exceptions
try:
    age = int(input("Age: "))
except ValueError as error:
    print("You did not enter a valid age.")
    print(error)
    print(type(error))
else:
    # this block will run if no exceptions are raised.
    print("No exceptions were raised.")
print("Execution continues.")
