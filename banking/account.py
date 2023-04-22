class Account:

    nextId = 0

    def __init__(self, description = 'New Account'):
        Account.nextId += 1
        self.id = Account.nextId
        self.description = description
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise Exception('amount cannot be zero or negative')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception('amount cannot be zero or negative')
        self.balance -= amount

    def transfer(self, amount, toAccount):
        self.withdraw(amount)
        toAccount.deposit(amount)

    def toString(self):
        return f'{self.id} | {self.description} | {self.balance}'   

