'''
A decorator feature in Python wraps in a function,
appends several functionalities to existing code and
then returns it. Methods and functions are known to be
callable as they can be called. Therefore, a decorator
is also a callable that returns callable. This is also
known as metaprogramming as at compile time a section
of program alters another section of the program.

    @property decorator is a built-in decorator in Python which
is helpful in defining the properties effortlessly without
manually calling the inbuilt function property(). Which is
used to return the property attributes of a class from the
stated getter, setter and deleter as parameters.
'''
class Portal:
    def __init__(self):
        self.__name = ''

    # Using property decorator
    # Getter method
    @property
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


'''
Here, the @property decorator is used to define the
property name in the class Portal, that has three
methods(getter, setter, and deleter) with similar names
i.e, name(), but they have different number of parameters.
'''
p = Portal()
# Setting name
p.name = 'Dracule Mihawk'
# Getting name
print(p.name)
# Deleting name
del p.name
''' Notice we haven't used brackets for functions'''
# As the name is deleted now, line below gives an error
print(p.name)
