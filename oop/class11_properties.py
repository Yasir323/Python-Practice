class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)
    # property takes 4 optional parameters:
    # 1st for getting the value of the attribute
    # 2nd for setting the value of the attribute
    # 3rd for deleting the attribute
    # 4th for documentation


product = Product(2050)
# We can set it this way too
product.price = -10
print(product.price)
# In this implementation  we have so many unwanteed functions
# which we should hide or get rid of.
