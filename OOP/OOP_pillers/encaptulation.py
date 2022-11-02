# Encapsulation is the process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.

# Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them.

# Encapsulation is used to achieve data hiding. Data hiding is a concept of restricting access to methods and variables. This prevents data from direct modification which is called encapsulation.


class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# Output:
# Selling Price: 900
# Selling Price: 900
# Selling Price: 1000