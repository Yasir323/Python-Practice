'''
A class method receives the class as implicit first argument,
just like an instance method receives the instance.
1. A class method is a method which is bound to the class
and not the object of the class.
2. They have the access to the state of the class as it
takes a class parameter that points to the class and not
the object instance.
3. It can modify a class state that would apply across
all the instances of the class. For example it can modify
a class variable that will be applicable to all the instances.
4. We generally use class method to create factory methods.
Factory methods return class object ( similar to a constructor )
for different use cases.
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


emp_1 = Employee('Yasir', 'Jafri', 500000)
emp_2 = Employee('John', 'Wick', 600000)

Employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.06) will also work but
# it will update it for emp_2 as well so there is no point
# of using it with an instance

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-700000'
emp_str_2 = 'Jane-Doe-300000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)

print(new_emp_2.email)
print(new_emp_2.pay)
