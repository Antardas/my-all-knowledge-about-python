class Shopper:

    def __init__(self, name):
        self.name = name
        self.quantity = []

    def add_to_cart(self, item, price, quantity):
        self.quantity.append({
            "item": item,
            "price": price,
            "quantity": quantity})
    def checkout(self):
        total = 0
        for item in self.quantity:
            total += item["price"] * item["quantity"]
        return total

shopper1 = Shopper("John")
shopper1.add_to_cart("Eggs", 2.50, 2)

shopper2 = Shopper("Mary")
shopper2.add_to_cart("Milk", 3.50, 1)
print(shopper1.checkout())
print(shopper2.checkout())
