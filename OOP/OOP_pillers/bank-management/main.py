""" Bank Management System """

class Account:
    accId = 1
    def __init__(self, name, age, nid_num, balance):
        self.name = name
        self.age = age
        self.nid_num  = nid_num
        self.balance = balance

        # Update account id
        self.account_id = Account.accId
        Account.accId +=1

    def deposit(self, amount):

        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount



acc_1 = Account("Antar", 19, 12345, 1000)

acc_1.deposit(200)

acc_2 = Account("Robin", 25, 12456, 1500)

acc_2.deposit(500)

acc_1.withdraw(520)
acc_2.withdraw(1020)

print(acc_1.balance, acc_2.balance)
