class Bottle:
    manufacturer = "Hawa"
    def __init__(self, brand, liter, price, features):
        self.brand = brand
        self.liter = liter
        self.price = price
        self.features = features
    def fill_water(self):
        print("Filling water")
    def fill_juice(self, fruit):
        print("Filling juice of " + fruit)


my_bottle = Bottle("Hawa", 1, 100, ["cold", "hot", "water", "juice"])

print(my_bottle.brand)
print(my_bottle.liter)
print(my_bottle.price)
print(my_bottle.features)

dad_bottle = Bottle("Pepsi", 2, 200, ["cold", "hot", "water", "juice"])

print(dad_bottle.brand)
print(dad_bottle.liter)
print(dad_bottle.price)
print(dad_bottle.features)

