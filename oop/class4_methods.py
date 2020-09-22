class Point:
    # Class Attributes
    default_color = "red"
    # Constructor

    def __init__(self, x=0, y=0):
        # Instance Attributes
        self.x = x
        self.y = y

    # Class method
    # It cannot be accessed by an instance
    @classmethod
    def zero(cls):
        return cls(0, 0)
        # This is similar to creating an instance with
        # arguments (0,0)

    # Instance method
    def draw(self):
        print(f"Point: ({self.x},{self.y})")


point = Point.zero()
point.draw()
