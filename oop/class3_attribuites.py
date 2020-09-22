class Point:
    # Class Attributes
    default_color = "red"
    # Constructor
    def __init__(self, x=0, y=0):
        # Instance Attributes
        self.x = x
        self.y = y

    # Class method
    def draw(self):
        print(f"Point: ({self.x},{self.y})")


point = Point(3, 4)
print(point.x)
point.draw()
point.z = 5
# We can access class attributes via instance:
print(point.default_color)
# Or via class name:
print(Point.default_color)
# Assignment: We can change the class attributes both
# via Class name and instance. But we can implement data
# hiding as well. Which we'll see later.
point.default_color = "yellow"
print(point.default_color)
print(point.default_color)
