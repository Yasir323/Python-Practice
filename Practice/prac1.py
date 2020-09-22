a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = (x for x in a if x <5)
for i in result:
    print(i)
