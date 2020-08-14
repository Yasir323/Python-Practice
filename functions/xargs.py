def multiply(*numbers: tuple) -> int:
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(multiply(1,2,3,5,6))
