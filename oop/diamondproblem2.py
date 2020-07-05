# WHEN METHOD IS OVERRIDDEN IN ONE OF THE CLASSES

# Python Program to depict multiple inheritance
# when method is overridden in one of the classes

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    pass


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()
