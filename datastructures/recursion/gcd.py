# GCD using recursion

def gcd(a, b):
    # Unintentional case
    assert int(a) == a and int(b) == b, "The numbers should be Integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    # Base case: gcd(a, 0) = 0
    if b == 0:
        return a
    # Recursive case: gcd(a, b) = gcd(b, a%b)
    else:
        return gcd(b, a % b)


print(gcd(48, 18))
