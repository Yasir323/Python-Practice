# Generators yield instead of return
def square_num(nums):
    for i in nums:
        yield(i*i)
n = [1,2,3,4,5]
for num in square_num(n):
    print(num)
