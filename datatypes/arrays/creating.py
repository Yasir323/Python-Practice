from array import array as arr

a = arr('i', [1, 2, 3])

# Printing the array
print("The array is: ", end='')
for i in range(0, 3):
    print(f"{a[i]:>6}", end='\t') # This is how we right allign our text

print() # This is how we print a newline in python

b = arr("d", [2.4, 546.56, 34.4])
print("The array is: ", end='')
for i in range(0, 3):
    print(f"{b[i]:>6}", end='\t')

print()
