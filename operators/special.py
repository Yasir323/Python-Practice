# a+=b is not alwasy equal to a=a+b
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]

print(list1)
print(list2)

list3 = [5, 4, 3, 2, 1]
list4 = list3
list3 = list3 + [1, 2, 3, 4]

# Contents of list1 are same as above
# program, but contents of list2 are
# different.
print(list3)
print(list4)
