class Animal:
    def eat(self):
        print("Eat")


class Mammal(Animal):
    def birth(self):
        print("No eggs")

class Tiger(Mammal):
    def movement(self):
        print("Walk")

class Fish(Animal):
    def movement(self):
        print("Swim")

    def birth(self):
        print("Lay eggs")

tuna = Fish()
tuna.movement()
tuna.eat()
tuna.birth()
sherkhan = Tiger()
sherkhan.movement()
sherkhan.eat()
sherkhan.birth()
