import array as arr

a = arr.array("i", [1, 2, 3, 4, 3])
print("The original array is: ", end ="")
for i in range(5):
    print(a[i], end = " ")
print()
# using remove(3) to remove the first occurence of 3
a.remove(3)
print ("The array after removing is : ", end ="")
for i in range (0, 4):
    print (a[i], end =" ")
print()
# using pop(2) to remove the element at index 2
a.pop(2)
print ("The array after popping is : ", end ="")
for i in range (0, 3):
    print (a[i], end =" ")
print()
'''
Note: remove take the element value as argument
but pop takes the index as argument.
So, if the element is not found, pop gives an index error
but remove gives value error
'''
