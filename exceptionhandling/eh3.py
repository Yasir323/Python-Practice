# Handling differennt exceptions
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age-1.")
except ZeroDivisionError:
    # In case of zero division error this block is not executed.
    # Since the above one is executed first.
    print("You didn't enter a valid age-2.")
else:
    print("No exceptions were raised.")

