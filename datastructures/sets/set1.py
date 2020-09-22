numbers = [1, 2, 3, 4, 5, 1]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first.union(second))
print(first & second)
print(first.intersection(second))
print(first - second)
print(first.difference(second))
print(first ^ second)
print(first.symmetric_difference(second))

# we cannot use indexing with sets to access it's elements
