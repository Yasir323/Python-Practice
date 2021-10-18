"""
Recurion is space inefficient as well as time inefficient.
But it is easier to implement when a large problem can be
divided into smaller sub-problems.
"""
# How recursion works?

def firstMethod():
    secondMethod()
    print("I am the first method.")


def secondMethod():
    thirdMethod()
    print("I am the second method.")


def thirdMethod():
    fourthMethod()
    print("I am the third method.")


def fourthMethod():
    print("I am the fourth method.")

firstMethod()
