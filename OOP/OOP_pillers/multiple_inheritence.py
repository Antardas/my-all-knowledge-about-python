# Multiple Inheritance
#

class Phone:
    def __init__(self, brand, model, price, camera):
        self.brand = brand
        self.model = model
        self.price = price
        self.camera = camera

    def __repr__(self) -> str:
        return f'{self.brand} - {self.model} - {self.price}'
    def run(self):
        print(f'''
        {self.brand} {self.model} is running...
        ''')

class Laptop:
    def __init__(self, brand, model, price, ram, storage, processor):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        self.storage = storage
        self.processor = processor

    def __repr__(self) -> str:
        return f'{self.brand} - {self.model} - {self.price}'
    def run(self):
        print(f'''
        {self.brand} {self.model} is running...
        ''')

class SmartPhone(Phone, Laptop):
    def __init__(self, brand, model, price, camera, ram, storage, processor):
        super().__init__(brand, model, price, camera)
        self.ram = ram
        self.storage = storage
        self.processor = processor

    def __repr__(self) -> str:
        return f'{self.brand} - {self.model} - {self.price}'
    def run(self):
        print(f'''
        {self.brand} {self.model} is running...
        ''')

smartphone = SmartPhone('Samsung', 'Galaxy S10', 50000, '12MP', '8GB', '1TB', 'i9')