

class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, num):
        off_price = (num / 100) * self.price
        return self.price - off_price


class Phone:

    def __init__(self, brand, model, price, camera):
        self.brand = brand
        self.model = model
        self.price = price


class Watch:

    def __init__(self, brand, model, price, water_resistant):
        self.brand = brand
        self.model = model
        self.price = price





