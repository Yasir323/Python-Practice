a, b = 10, 20
min = a if a < b else b
print(min)

# Using Tuple
print((b, a)[a < b])

# Using dict'
print({True: a, False: b} [a < b])

# Using lambda
print((lambda: b, lambda: a)[a < b]())

# Nested
print("Both a and b are equal" if a == b else "a is greater than b"
       if a > b else "b is greater than a")
