class MyClass:
    # Hidden member of class is named
    # using two underscores at the
    # start of the name
    __hiddenVariable = 0

    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


myObject = MyClass()
myObject.add(2)
myObject.add(10)
# Following line causes an error because we are trying
# to access a variable that is private to the class

# print(myObject.__hiddenVariable)

# If we really want to access that varible
# then we have to do this
print(myObject._MyClass__hiddenVariable)
