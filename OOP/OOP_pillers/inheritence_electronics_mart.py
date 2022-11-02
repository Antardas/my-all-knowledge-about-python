class Device:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self) -> str:
        return f'{self.brand} - {self.model} - {self.price}'
    def run(self):
        print(f'''
        {self.brand} {self.model} is running...
        ''')


class Laptop(Device):

    def __init__(self, brand, model, price, ram, storage, processor):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage
        self.processor = processor



    def apply_discount(self, num):
        off_price = (num / 100) * self.price
        return self.price - off_price


class Phone(Device):

    def __init__(self, brand, model, price, camera, ram):
        super().__init__(brand, model, price)
        self.camera = camera
        self.ram = ram


class Watch(Device):

    def __init__(self, brand, model, price, water_resistant):
        super().__init__(brand, model, price)
        self.water_resistant = water_resistant



laptop_lenovo = Laptop('Lenovo', 'Thinkpad', 50000, '8GB', '1TB', 'i5')

hp = Laptop('HP', 'Pavilion', 60000, '8GB', '1TB', 'i9')

phone_samsung = Phone("Samsung", "Galaxy S10", 50000, "12MP", "8GB")

watch_apple = Watch("Apple", "Apple Watch", 50000, True)

print(laptop_lenovo)

print(hp)

print(phone_samsung)

print(watch_apple)