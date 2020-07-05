#COMMAND LINE ARGUMENTS

#Importing CLA
from sys import argv
#Unpacking or saving these arguments in variables
script, first, second, third = argv

#printing these ARGUMENTS
print("The script is called: ", script)
print(f"The first argument is: {first}")
print("The second argument is: %s" %second)
print("The third argument is: ", third)
