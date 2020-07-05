# WHEN EVERY CLASS DEFINES THE SAME METHOD

# Python Program to depict multiple inheritance
# when every class defines the same method

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
    def m(self):
        print("In Class4")


obj = Class4()
obj.m()
'''
The output of the method obj.m() in the above code is In Class4.
The method “m” of Class4 is executed. To execute the method “m”
of the other classes it can be done using the class names.
'''
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
