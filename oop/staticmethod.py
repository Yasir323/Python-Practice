# STATIC METHOD
'''
A static method does not receive an implicit first argument.
1. A class method is a method which is bound to the class
    and not the object of the class.
2. They have the access to the state of the class as it takes
    a class parameter that points to the class and not the
    object instance.
3. It can modify a class state that would apply across all
     the instances of the class. For example it can modify a
     class variable that will be applicable to all the instances.
4. We generally use static methods to create utility functions.
'''
class Employee:
    # Class Variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = last + '.' + first + '@company_name.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # A class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Class method as a constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Yasir', 'Jafri', 500000)
emp_2 = Employee('John', 'Wick', 600000)

import datetime
my_date = datetime.date(2020, 6, 18)
print(Employee.is_workday(my_date))
