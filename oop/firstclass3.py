# PROGRAM TO ILLUSTRATE THAT FUNCTIONS CAN
# RETURN ANOTHER FUNCTION
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add = create_adder(15)(10)
# x is 15 and y is 10
print(add)

# or we can also do it the following way
add = create_adder(15)
print(add(10))
