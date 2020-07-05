'''
1. str() is used for creating output for end user while
repr() is mainly used for debugging and development.
repr’s goal is to be unambiguous and str’s is to be readable.
For example, if we suspect a float has a small rounding error,
repr will show us while str may not.
2. repr() compute the “official” string representation of
an object (a representation that has all information about
the object) and str() is used to compute the “informal”
string representation of an object (a representation that
is useful for printing the object).
3. The print statement and str() built-in function uses
__str__ to display the string representation of the object
while the repr() built-in function uses __repr__ to display
the object.

If str or repr methods are not defined and we try to
print the class or instance, Python prints out the location
of the class object in the memory.
'''
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s b: %s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s" \
                "b is %s" % (self.a, self.b)


t = Test(1234, 5678)
print(t)    # This calls __str__()
print([t])  # This calls __repr__()
'''
 IF NO __str__ METHOD IS DEFINED THEN PRINT USES __repr__
 AND IF BOTH THE METHODS AREN'T THERE THEN DEFAULT IS CALLED
 WHICH PRINTS OUT THE ADDRESS OF CLASS
'''
