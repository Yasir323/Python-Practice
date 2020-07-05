"""
1. Python considers empty strings as having
boolean value of ‘false’ and non-empty
string as having boolean value of ‘true’.

2. For ‘and’ operator if left value is true,
then right value is checked and returned.
If left value is false, then it is returned.

3.For ‘or’ operator if left value is true,
then it is returned, otherwise if left value
is false, then right value is returned
"""

str1 = ''
str2 = 'geeks'

# repr is used to print the string along with the quotes


print(repr(str1 and str2))	 # Returns str1
print(repr(str2 and str1))	 # Returns str1
print(repr(str1 or str2))	 # Returns str2
print(repr(str2 or str1))	 # Returns str2

str1 = 'for'

print(repr(str1 and str2))	 # Returns str2
print(repr(str2 and str1))	 # Returns str1
print(repr(str1 or str2))	 # Returns str1
print(repr(str2 or str1))	 # Returns str2

str1 = 'geeks'


print(repr(not str1))		 # Returns False

str1 = ''

print(repr(not str1))		 # Returns True
