
from account import Account

# Check deposit and withdraw with USD
acc = Account("Abu")

acc.deposit(100, "USD")
balance1 = acc.balance
assert balance1 > 900 and balance1 < 1000 , f"Unexpected value returned, got {acc.balance}"


acc.withdraw(50)
balance2=acc.balance
assert (balance1 - balance2) == 50, f"Expected 50, got {balance1 - balance2}"


# Check deposit and withdraw with EURO
acc = Account("Abu")

acc.deposit(100, "EUR")
balance1 = acc.balance
assert balance1 > 1000 and balance1 < 1200 , f"Unexpected value returned, got {acc.balance}"

