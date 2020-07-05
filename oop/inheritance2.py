'''
Example to show that base class members
can be acessed in derived class using
"BASE CLASS NAME"
'''


class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(Base.x, self.y)
        # print(self.x, self.y) will also work


# Driver code
d = Derived(10, 20)
d.printXY()
