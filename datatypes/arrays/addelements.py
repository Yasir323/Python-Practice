import array as arr

a = arr.array("i", [1, 2, 3])
for i in range(3):
    print(a[i], end = "")
print()

a.insert(1, 4)      # Insert 4 at position with index 1
print ("Array after insertion : ", end =" ")
for i in range (0, 4):
    print (a[i], end =" ")
print()

# We can also use append()
a.append(5)
print ("Array after appending : ", end =" ")
for i in range (0, 5):
    print (a[i], end =" ")
print()
