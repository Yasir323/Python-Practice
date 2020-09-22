import sys

try:
    num = int(input("Enter number: "))
except ValueError:
    print("You did not enter a valid number.")
    sys.exit(1)
if num >= 2:
    for i in range(2, int((num/2) + 1)):
        if num % i == 0:
            print("Not a prime number.")
            sys.exit(0)
    print("Prime number.")
elif num < 0:
    print("Not a valid number.")
else:
    print("Not a prime number")
