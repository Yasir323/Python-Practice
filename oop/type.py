'''
We can create classes using type() function directly.
It can be called in following ways –
1. When called with only one argument, it returns the type.
We have seen it before in above examples.
2. When called with three parameters, it creates a class.
Following arguments are passed to it –
    Class name
    Tuple having base classes inherited by class
    Class Dictionary: It serves as local namespace for the class,
    populated with class methods and variables
'''
def test_method(self):
    print("This is a test method.")

# Creating the base class
class Base:
    def myfun(self):
        print("This is inherited method.")

# Creating Test class dynamically using the type() method
Test = type("Test", (Base, ), dict(x = "Test class attribute", my_method = test_method))

# Printing the type of the Test class
print("Type of the Test classs: ", type(Test))
# creating instance of the class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# Calling inherited method
test_obj.myfun()

# Callling Test class method
test_obj.my_method()

# Printing the class variable
print(test_obj.x)


