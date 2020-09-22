nums = [x for x in range(5)]
print(nums)

print("Using unpack operator:")
print(*nums)

print("Declaration")
values = list(range(10))
print(values)
print("Using unpack operator:")
values = [*range(10), nums]
print(values)
values = [*range(10), *nums]
print(values)

print("Unpacking dictionaries:")
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second}
print(combined)
