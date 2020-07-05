# Addition of two complex numbers using overloading of binary
# '+' operator

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    # def __str__(self):
    #     return self.a, self.b


ob1 = Complex(1, 2)
ob2 = Complex(2, 3)
print(ob1 + ob2)
