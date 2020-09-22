# Unpacking and packing
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
print(f"{first}\t{second}\t{third}")
print("It's the same as the following unpacking:")
first, second, third = numbers
print(f"{first}\t{second}\t{third}")
print("Let's get a bit crazy!")
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
_, _, _, fourth, fifth, sixth, _, _ = numbers2
print(f"{fourth}\t{fifth}\t{sixth}")
print("Let's try Unpacking 'numbers2' and then pack some of it in 'trash'")
_, *trash, seventh, eighth = numbers2
print(f"This is trash: {trash}\n{seventh}\t{eighth}")
