# WHILE LOOP
i = 0
numbers = []

while i < 6:
    print(f"At the top i is: {i}")
    numbers.append(i)
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is: {i}")

print("The numbers:    ", end = ' ')

for num in numbers:
    print(f"{num}\t", end = ' ')
