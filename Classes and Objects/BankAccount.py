class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

account1 = BankAccount("Tamanappa", 20000)
account1.deposit(5000)
account2 = BankAccount("Suraj", 30000)
account2.withdraw(10000)

print(account1.balance)
print(account2.balance)


