class Account:
    def __init__(self, name, currency="SEK"):
        self.name = name
        self.balance = 0.0
        self.currency = currency
        # add empty transaction list to store transaction history
        self.transactions = []  # list of dicts

    # Method deposit
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            self.balance += amount
            self._log("deposit", amount)
        
        except Exception as e:
            print(f"Amount error: {e}")

    # Method withdraw    
    def withdraw(self, amount):
        try:
            if amount<= 0:
                raise ValueError("Amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds!")
            self.balance -= amount
            self._log("withdraw", amount)
        
        except Exception as e:
            print(f"Amount error: {e}")
    
    # Method logging transactions
    def _log(self, type, amount):
        entry = {
            "type": type,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transactions.append(entry)

    # Method show balance
    def get_balance(self):
        return self.balance
