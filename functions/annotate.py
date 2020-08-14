# Function annotations
def factorial(n:int) -> int:
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Invalid number.")
    else:
        return n * factorial(n - 1)

try:
    number = -1
    print(factorial(number))
except ValueError as error:
    print(error)
