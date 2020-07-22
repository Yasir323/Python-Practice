import copy

ls1 = [x for x in range(10) if x % 2 == 1]
print("ls1:",ls1)

ls2 = ls1
print("ls2:",ls2)
# Changes made to any element of existing lists or appended to them will
# be reflectedto both the lists
ls2.append(99)
ls1.append(98)
ls2[0] = 1000

print(f"ls1: {ls1}")
print("ls2:",ls2)
# --------------------------------------------------------------------------------------------
'''
Shallow copy:
New elements created in new list will not be created in old list
but changes made to existing elements will be reflected.
'''
ls5=copy.copy(ls1)
print("ls5:",ls5)
ls5.append(78)
ls1.append(77)
ls5[1]=999
print("ls1:",ls1)
print("ls5:",ls5)
# ---------------------------------------------------------------------------------------------

ls3=ls1.copy()
print("ls3:",ls3)
ls3.append(43)
ls1.append(42)
ls3[2]=998
print("ls1:",ls1)
print("ls3:",ls3)
# ---------------------------------------------------------------------------------------------
# Exactly similar to shallow copy
ls4=ls1[:]
print("ls4:",ls4)
ls4.append(51)
ls1.append(50)
ls4[3]=997
print("ls1:",ls1)
print("ls4:",ls4)
# -----------------------------------------------------------------------------------------------
ls6=copy.deepcopy(ls1)
print("ls6:",ls6)
ls6.append(63)
ls1.append(62)
ls6[4]=996
print("ls1:",ls1)
print("ls6:",ls6)
