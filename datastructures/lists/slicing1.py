# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst =list(range(1, 11))
print (lst)

# below list has numbers from 2 to 5
lst1_5 = lst[1 : 5]
print (lst1_5)

# below list has numbers from 6 to 8
lst5_8 = lst[5 : 8]
print (lst5_8)

# below list has numbers from 2 to 10
lst1_ = lst[1 : ]
print (lst1_)

# below list has numbers from 1 to 5
lst_5 = lst[: 5]
print (lst_5)

# below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1 : 8 : 2]
print (lst1_8_2)

# below list has numbers from 10 to 1
lst_rev = lst[ : : -1]
print (lst_rev)

# below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9 : 4 : -2]
print (lst_rev_9_5_2)
