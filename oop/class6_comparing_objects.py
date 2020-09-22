class Point:
    # Constructor
    def __init__(self, x=0, y=0):
        # Instance Attributes
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other_point = Point(10, 20)
print(point < other_point)
# Now we don't need to explicitly define less than
# method after defining greater than method, Python will
# automatically find out what to do once we define
# grater than.
