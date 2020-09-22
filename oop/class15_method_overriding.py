# Method overriding is the process of a class replacing a method
# defined in it's parent class by it's own method.

class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self): # This constructor will override the one defined in 'Animal'
        super().__init__()  # To access the constructor in Animal
        self.weight = 2

    def birth(self):
        print("No eggs")


m = Mammal()
print(m.age)
print(m.weight)

