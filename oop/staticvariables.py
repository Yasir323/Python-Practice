# Python program to show that the variables with a value
# assigned in class declaration, are class variables
'''
Class or static variables are shared by all objects.
Instance or non-static variables are different for
different objects (every object has a copy of it).
'''
# Class for Computer Science Student
class CSStudent:
	# Class Variable
	stream = 'cse'

	def __init__(self,name,roll):
		self.name = name	# Instance Variable
		self.roll = roll	# Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also but they cannot be changed that's
# why it is called static
print(CSStudent.stream) # prints "cse"
