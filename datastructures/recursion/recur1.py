import sys

"""
Let's increse recursion limit, although we don't need it,
since we are trying to avoid it.
"""
# sys.setrecursionlimit(10000)
def factorial(n):
    # Unintentional case - The constraint
    assert n >= 0 and int(n) == n, "You did not enter a POSITIVE INTEGER!!!"

    # Base condition
    if n in [0, 1]:
        return 1

    # Recursive condition
    else:
        return n * factorial(n - 1)

n = int(input("Enter a positive integer: "))
print(factorial(n))
