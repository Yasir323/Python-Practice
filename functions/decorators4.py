# Giving a function as an argument to another function

def hi():
    return "Hi, Yasir."


def doSomethingBeforeHi(func):
    print("Before hi.")
    print(func())


doSomethingBeforeHi(hi)
