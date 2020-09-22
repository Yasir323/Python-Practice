# Constructor
'''
It is one of the special methods called magic methods.
Magic methods' name are prefixed and suffixed with 2 double underscores.
All the classes are by-default instances of a super class called 'object'.
And these magic methods are defined for that super class 'object'.
So these methods are inherited by all the classes we define.
We can choose to redefine some or all  of these special methods.
'''
from math import sqrt

class Point:
    # Constructor
    def __init__(self, x=0, y=0):
        # Attributes
        self.x = x
        self.y = y

    # Class method
    def draw(self):
        print(f"Point: ({self.x},{self.y})")

    def position_vector(self):
        return sqrt((self.x ** 2) + (self.y ** 2))


# 'self' is a refernce to the class' instance. When an instance is
# instanciated the self is replaced by that instance.
point = Point(3, 4)
print(point.x)
point.draw()
print(point.position_vector())
# We can also define an attribute after we define an object
# because objects in Python are dynamic. So we do not need to define
# all the attributesw in the constructor, we can define them as needed.
point.z = 5
# But now we cannot call the methods since they take only two arguments.
