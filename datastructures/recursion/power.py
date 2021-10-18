# Power of a number using recursion

def Power(x, n):
    # Unintentional case
    assert n >= 0 and int(n) == n, "The exponent has to be a non \
    negative integer"
    assert x >= 0 and int(x) == x, "The exponent has to be a non \
    negative integer"
    # Base case
    if n == 1:
        return x
    # Recursive case
    else:
        return x * Power(x, n - 1)


print(Power(5, 4))
