# PROGRAM TO PRINT LIST OF VALID A KEYWORD

import keyword

print("The list of valid keywords in Python is:")
list = keyword.kwlist
for i in range(len(list)):
    print(list[i])
