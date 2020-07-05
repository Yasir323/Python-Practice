# USING LOOP ONLY

def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    return str


str = input("Enter string: ")
print("Original string: {}".format(str))
rev = reverse_string(str)
print("Reversed string: %s"%rev)
