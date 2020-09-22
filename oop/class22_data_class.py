# Data classes are the one which don't have any method
from collections import namedtuple as nt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
# This will return false becoz these instances are stored
# at different locations and Python compares objects by
# comparing their memory locations. To get away with this
# we neeed to implement __eq__ method to work differently

# But this much work for data classes is not worth it,
# instead we must use named tuple

Coordinate = nt("Coordinate", ["x", "y"])
p = Coordinate(x=1, y=2)
q = Coordinate(x=1, y=2)
print(p == q)
print(p.x)
# Now the code loooks much more cleaner and shorter.
# But there is one catch, these objects are immutable so we
# cannot change them.
