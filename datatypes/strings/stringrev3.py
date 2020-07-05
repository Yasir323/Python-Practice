# USING RECURSION
def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]


s = input("Enter string: ")
rev = reverse(s)
print(f"Reversed string: {rev}")
