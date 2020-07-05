# PROGRAM TO SHOW THAT THE VARIABLES WITH A VALUE ASSIGNED
# IN CLASS DECLARATION, ARE CLASS VARIABLES AND VARIABLES INSIDE
# METHODS AND CONSTRUCTORS ARE INSTANCE VARIABLES

class Student:
    # Class variable:
    stream = 'cse'

    # Constructor
    def __init__(self, roll):
        # Instance variable
        self.roll = roll


# Instance of Student class
a = Student(101)
b = Student(102)

print(a.stream, a.roll)
'''
If stream is a class variable, why can we access it through an instance?
Shouldn't it be: Strudent.stream?
What Python does is that it searches in the instance, then it class and
then any superclass if available.
'''
print(Student.stream, a.roll)
print(b.stream, b.roll)
'''
Let's print something more interesting.
'''
print(a.__dict__)
print(Student.__dict__)
'''
Let's change the class variable for instance "a".
Notice another addition to it's dictionary.
'''
a.stream = 'cs'
print(a.__dict__)
print(a.stream, a.roll)
print(Student.__dict__)
