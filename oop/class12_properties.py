class Product:
    def __init__(self, price):
        self.__price = price

    @property    # To create a property object
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value



product = Product(2050)
# We can set it this way too
product.price = -10
print(product.price)
