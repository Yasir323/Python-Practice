'''
It refers to an ambiguity that arises when two classes
Class2 and Class3 inherit from a superclass Class1 and
class Class4 inherits from both Class2 and Class3.
If there is a method “m” which is an overridden method
in one of Class2 and Class3 or both then the ambiguity
arises which of the method “m” Class4 should inherit.
'''

# WHEN METHOD IS OVERRIDDEN IN BOTH CLASSES

# Python Program to depict multiple inheritance
# when method is overridden in both classes


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()

'''
If Class4 is defined as:-
Class4(Class3, Class2:)
Then the output will be:-
In Class2
'''
