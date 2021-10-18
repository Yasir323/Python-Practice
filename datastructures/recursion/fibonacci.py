def fib(n):
    # Unintentional case
    assert n >= 0, "Enter a POSITIVE INTEGER."

    # Base case
    if n in [0, 1]:
        return n

    # Recursive case
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter size of Fibonacci sequence you want: "))
print(fib(n - 1))
