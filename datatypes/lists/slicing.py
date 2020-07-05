def pop_list(list):
    for i in range(k):
        if len(list):
            list.pop(0)
k = 5
list = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(list)
print(list)
list2 = []
new_list = []
for i in range(int(n / k) + 1):
    list2.extend(list[0:k])
    list2.reverse()
    new_list.extend(list2)
    list2.clear()
    pop_list(list)
print(new_list)

