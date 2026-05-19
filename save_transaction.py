import json

class Save:
    @staticmethod
    def save_transaction(account, filename="account.json"):
        data = {
            "name": account.name,
            "balance": account.balance,
            "currency": account.currency,
            "transactions": account.transactions
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
