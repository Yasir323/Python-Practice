class Animal:
    def eat(self):
        print("Meat")


class Mammal(Animal):
    def birth(self):
        print("No eggs")

class Lion(Mammal):
    def movement(self):
        print("Walks.")


simba = Lion()
simba.eat()
