class Shopping:

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    @staticmethod
    def calculate_product_price(price, quantity):
        return price * quantity

    def add_to_cart(self, item):
        self.items.append(item)


cstm_1 = Shopping("Abul")

print(cstm_1.calculate_product_price(10, 20))
