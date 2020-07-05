'''
A Class is also an object, and just like any other object
it’s a instance of something called Metaclass. A special
class called 'type' creates these Class object. The 'type'
class is default 'metaclass' which is responsible for
making classes.
So, Metaclass create Classes and Classes creates objects.
'''
# Defined class without any class methods and variables
class test:
    pass

# Defining method variables
test.x = 45

# Defining class methods
test.foo = lambda self: print('Hello')

# creating object
myobj = test()

print(myobj.x)
myobj.foo()
print(test.__dict__)
