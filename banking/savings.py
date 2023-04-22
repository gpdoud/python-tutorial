from account import Account

class Savings(Account):

    def __init__(self, description):
        super().__init__(description)
        self.intRate = 0.12

    def payInterest(self, months):
        interest = self.balance * (self.intRate / 12) * months
        self.deposit(interest)