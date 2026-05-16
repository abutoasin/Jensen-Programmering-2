class Account:
    def __init__(self, name, currency="SEK"):
        self.name = name
        self.balance = 0.0
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
