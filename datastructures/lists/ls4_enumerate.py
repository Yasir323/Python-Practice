# Looping over lists with Enumerate
# enumerate is an iterator object
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
print("Unpacking letter and index")
for index, letter in enumerate(letters):
    print(index, letter)
