# Here is my generator
# They save only one value at a line in the memory
my_nums = (x**2 for x in range(5))
print(my_nums)
for num in my_nums:
    print(num)
