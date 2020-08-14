# cleaning up
try:
    file = open("New Text Document.txt")
    age = int(input("Age: "))
    xfactor = 10 / age
    # Now if the age is zero the file will not be closed,
    # if the close file statement is in this block
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")
else:
    print("No exceotions were thrown.")
finally:
    # This block is always executed whether we have an exception or not.
    file.close()
# BTW we can ahieve this using the with statement much more easily

