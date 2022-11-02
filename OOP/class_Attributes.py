class Shop:
    cart = []

    def __init__(self, buyer):
        self.name = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


shop1 = Shop("John")

shop1.add_to_cart("Milk")
shop1.add_to_cart("Bread")

shop2 = Shop("Mary")

shop2.add_to_cart("Eggs")
shop2.add_to_cart("Butter")

print(shop1.cart)
print(shop2.cart)
