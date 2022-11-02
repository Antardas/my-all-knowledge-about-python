class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if(amount >= self.min_withdraw and amount <= self.max_withdraw):
            self.balance -= amount
            return amount


AB_bank = Bank(10000)
print(AB_bank.get_balance())
print(AB_bank.withdraw(1000))