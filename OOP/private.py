class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password
    


akib = User('Akib', 'antardas2334@gmail.com', 'mysecretpassword')


print(akib.password)
