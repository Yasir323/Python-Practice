# using extended slicing syntax
def reverse(str):
    str = str[::-1]
    return str


s = input("Enter string: ")
print(f"Reversed string: {reverse(s)}")
