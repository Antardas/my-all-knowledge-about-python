class Bottle:
    brand = "Hawa"
    liter = 1
    price = 100
    features= ["cold", "hot", "water", "juice"]
    def fillWater(self):
        print("Filling water")
    
    def fillJuice(self, fruit):
        print("Filling juice of " + fruit)
    


my_bottle = Bottle()

my_bottle.fillWater()

my_bottle.fillJuice("Apple")



