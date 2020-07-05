# SUPER FUNCTION WITH ARGUMENTS
class Square:
	def __init__(self, side):
		self.side = side

	def area(self):
		return self.side * self.side


'''
Note: Since Cube class does not have an __init__() method,
the __init__() of Square class will be used for
initialization of Cube instances (basic property of inheritance).
'''


class Cube(Square):
	def area(self):
		return super().area() * 6
		# super(Cube, self).area() will also work
		# Square.area() will work too

	def volume(self):
		return super().area() * self.side
