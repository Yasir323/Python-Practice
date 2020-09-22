# Sorting


letters = ["a", "b", "c", "d", "c"]
print(f"Original:{letters}")

# Sort method
# This method changes the list order permanently
letters.sort()
print(f"Sorted: {letters}")
letters.sort(reverse=True)
print(f"Sorted: {letters}")

numbers = [2,324,234,243,21,112,131,3123,3,12,12321,3,]
print(f"Original: {numbers}")
numbers.sort()
print(f"Sorted: {numbers}")
numbers.sort(reverse=True)
print(f"Sorted: {numbers}")

# ls = numbers + letters
# ls.sort()
# print(ls)
# The above snippet of code won't work as we cannot sort
# a non-homogenous list

# Sorted iterator
# Doesn't alter the original list
numbers2 = [3, 2, 1, 4, 5]
print(sorted(numbers2))
print(sorted(numbers2, reverse=True))
print(numbers2)
