# Python code to demonstrate
# searching an element in array


# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print ("The new created array is : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")

print ("\r")

# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ", end ="")
print (arr.index(2))

# using index() to print index of 1st occurrenece of 1
print ("The index of 1st occurrence of 1 is : ", end ="")
print (arr.index(1))
