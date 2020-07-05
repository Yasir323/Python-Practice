'''
Example to show that base class members
can be acessed in derived class using
            "super()"
'''


class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        super(Derived, self).__init__(x)
        # super().__init__(x) will also work
        self.y = y

    def printXY(self):
        print(self.x, self.y)
        # print(Base.x, self.y) will NOT work her


# Driver code
d = Derived(10, 20)
d.printXY()
