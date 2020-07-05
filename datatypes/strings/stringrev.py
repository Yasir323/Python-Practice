# USING LIST

str1 = input("Enter the word: ")
list1 = []
for i in range(len(str1)):
    list1.append(str1[i])

list1.reverse()
str2 = "".join(list1)
print(str2)
