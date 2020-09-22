# Program to remove all non-alphabetical characters
# from a given string
str = "$Gee*k;s..fo, r'Ge^eks?"
list = []
for i in range(len(str)):
    if (str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z'):
        list.append(str[i])
print("".join(list))
