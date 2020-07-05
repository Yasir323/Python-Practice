'''
To list the attributes of an instance/object, we have two functions:-
1. vars()– This function displays the attribute of an instance in the
   form of an dictionary.
2. dir()– This function displays more attributes than vars function,
   as it is not limited to instance. It displays the class attributes
   as well. It also displays the attributes of its ancestor classes.
'''

# Python program to demonstrate
# instance attributes.
class emp:
    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000

    def show(self):
        print(self.name)
        print(self.salary)

e1 = emp()
print("Dictionary form :", vars(e1))
print(dir(e1))
