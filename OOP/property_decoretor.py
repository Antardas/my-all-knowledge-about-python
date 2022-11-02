class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name}.{last_name}@google.com'
    # Function Decorator
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    # Function Decorator with Setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last
    
    

abul = User('Abul', "Hasan")

print(abul.fullname)

abul.fullname = "Kabul Hasan"
print(abul.fullname)