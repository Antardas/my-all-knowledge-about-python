# Multi Level Inheritance


class Phone:

    def __init__(self, brand, model, price, screen_size):
        self.brand = brand
        self.model = model
        self.price = price
        self.screen_size = screen_size

    def __repr__(self) -> str:
        return f'{self.brand} - {self.model} - {self.price}'


class SmartPhone(Phone):

    def __init__(self, brand, model, price, screen_size, camera):
        super().__init__(brand, model, price, screen_size)
        self.camera = camera


class FlagshipPhone(SmartPhone):

    def __init__(self, brand, model, price, screen_size, camera, ram, storage,
                 processor):
        super().__init__(brand, model, price, screen_size, camera)
        self.ram = ram
        self.storage = storage
        self.processor = processor
    def runFlagshipPhone(self):
        print(f'''
        {self.brand} {self.model} is running...
        ''')


simple_phone = Phone('Nokia', '1100', 1000, '2.4')
print(simple_phone)
samsung_galaxy_s10 = FlagshipPhone('Samsung', 'Galaxy S10', 60000, '6.1',
                                   '12MP', '8GB', '128GB', 'Snapdragon 855')

print(samsung_galaxy_s10)
normal_smartphone = SmartPhone('Samsung', 'Galaxy S10', 60000, '6.1', '12MP')
print(normal_smartphone)

samsung_galaxy_s10.runFlagshipPhone()


# Multilevel Inheritance - Inheritance of a derived class from another derived class is called multilevel inheritance. In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class. The syntax for multilevel inheritance is similar to that of single inheritance. The only difference is that we derive a class from a derived class.
