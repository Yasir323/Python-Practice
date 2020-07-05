'''
Type Conversion in Python

1. int(a,base) : This function converts any data type to integer.
‘Base’ specifies the base in which string is if data type is string.
2. float() : This function is used to convert any data type to a
floating point number.
3. ord() : This function is used to convert a character to integer.
4. hex() : This function is to convert integer to hexadecimal string.
5. oct() : This function is to convert integer to octal string.
6. tuple() : This function is used to convert to a tuple.
7. set() : This function returns the type after converting to set.
8. list() : This function is used to convert any data type to a list type.
9. dict() : This function is used to convert a tuple of order (key,value)
into a dictionary.
10. str() : Used to convert integer into a string.
11. complex(real,imag) : : This function converts real numbers to
complex (real,imag) number.
12. chr(number) : : This function converts number to its corresponding
ASCII character.
'''
# Python code to demonstrate Type conversion
# using int(), float()

# initializing string
s = "10010"

# printing string converting to int base 2
a = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (a)

# printing string converting to int base 10
b = int(s,10)
print ("After converting to integer base 10 : ", end="")
print (b)

# printing string converting to float
c = float(s)
print ("After converting to float : ", end="")
print (c)

# Python code to demonstrate Type conversion
# using ord(), hex(), oct()

# initializing integer
s = '4'

# printing character converting to integer
d = ord(s)
print ("After converting character '4' to integer, it's ASCII value is : ",end="")
print (d)

# printing integer converting to hexadecimal string
e = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (e)

# printing integer converting to octal string
f = oct(56)
print ("After converting 56 to octal string : ",end="")
print (f)

# Python code to demonstrate Type conversion
# using tuple(), set(), list()

# initializing string
s = 'geeks'

# printing string converting to tuple
g = tuple(s)
print ("After converting string to tuple : ",end="")
print (g)

# printing string converting to set
h = set(s)
print ("After converting string to set : ",end="")
print (h)

# printing string converting to list
i = list(s)
print ("After converting string to list : ",end="")
print (i)

# Python code to demonstrate Type conversion
# using dict(), complex(), str(), ord()

# initializing integers
a = 1
b = 2

# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))

# printing integer converting to complex number
j = complex(a,b)
print ("After converting integer to complex number : ",end="")
print (j)

# printing integer converting to string
k = str(a)
print ("After converting integer to string : ",end="")
print (k)

# printing tuple converting to expression dictionary
l = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (l)

print(chr(76))
print(chr(77))

