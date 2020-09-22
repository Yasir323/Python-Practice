class Employee:
    def greet(self):
        print("Employee greet.")


class Person:
    def greet(self):
        print("Employee greet.")


class Manager(Employee, Person):
    pass


man = Manager()
man.greet() # Employee greet will be called because
# it's name is written first in class definition of Manager.
''
