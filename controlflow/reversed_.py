'''
Using reversed(): reversed() is used to print the values of container in the reversed order.
Note: It does not reflect any changes to the original list
'''

# initializing list
lis = [ 1 , 3, 5, 6, 2, 1, 3 ]


# using revered() to print the list in reversed order
print ("The list in reversed order is : ")
for i in reversed(lis) :
    print (i,end=" ")
