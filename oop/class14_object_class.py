# Object is the base class for all classes by default and hence all the classes
# inherit from it.
class Animal:
    def eat(self):
        print("Eat")

tiger = Animal()
print(isinstance(tiger, object))
print(issubclass(Animal, object))
