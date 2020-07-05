# OVERLOADING BINARY + OPERATOR

class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Yasir")
ob4 = A("Jafri")

print(ob1 + ob2)
print(ob3 + ob4)
