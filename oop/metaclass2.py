'''
To create our custom metaclass, our custom metaclass have
to inherit type metaclass and usually override –
1. __new__(): It’s a method which is called before __init__().
It creates the object and return it. We can overide this
method to control how the objects are created.
2. __init__(): This method just initialize the created object
passed as parameter
'''
# Following program will show the way to create a metaclass called
# Multibases which will check if class being created has inherited
# from more than one base classes. If so, raise an error.

# Creating Metaclass
class Multibases(type):
    # Overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # If number of base classes is greater than 1, raise error
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!")

        # else execute __new__ method of super class, i.e.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)

# metaclass can be specified by metaclass keyword argument
# now Multibases class is used for cvreating classes
# This will also be propogated to all subclasses of base
class Base(metaclass = Multibases):
    # Now our base class does not have type as its metaclass,
    # its base class if now Multibases
    pass

class A(Base):
    pass
    # No error

class B(Base):
    pass
    # No error

class C(A, B):
    pass
    # This will raise an error
