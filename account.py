class Account:
    def __init__(self, name, currency="SEK"):
        self.name = name
        self.balance = 0.0
        self.currency = currency
        # add empty transaction list to store transaction history
        self.transactions = []  # list of dicts

    def deposit(self, amount):
        self.balance += amount
        self._log("deposit", amount)

    def withdraw(self, amount):
        self.balance -= amount
        self._log("withdraw", amount)
    # logging transactions
    def _log(self, type, amount):
        entry = {
            "type": type,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transactions.append(entry)

    def get_balance(self):
        return self.balance
