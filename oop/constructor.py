class person:
    # init method or constructor
    def __init__(self, name):
        print("Inside constructor")
        # initialize the string to be passed by object of the class
        self.name = name

    def say_hi(self):
        print(f"Hello, {self.name}")


p = person("Yasir")
p.say_hi()
