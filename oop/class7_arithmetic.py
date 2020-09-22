class Point:
    # Constructor
    def __init__(self, x=0, y=0):
        # Instance Attributes
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


point = Point(1, 2)
other_point = Point(10, 20)
print(point + other_point)
