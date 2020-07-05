# A Python program to inheritance

# Base class or Super Class. Note object in bracket.
# Generally, object is made ancestor of all classes.
# In Python 3, "class MyClass" is equivalent to
# "class MyClass(object)"

# Base class or super class
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited class or subclass
class Employee(Person):

    # Here wereturn True
    def isEmployee(self):
        return True


# Driver code

# To check which class is Base and which is inherited
print(issubclass(Person, Employee))
print(issubclass(Employee, Person))

emp = Person("Mohan")   # An object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Rohan")     # An object of Employee
print(emp.getName(), emp.isEmployee())
