from account import Account

class SavingsAccount(Account):
    def __init__(self, name, interest_rate=0.01, currency="SEK"):
        super().__init__(name, currency)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
