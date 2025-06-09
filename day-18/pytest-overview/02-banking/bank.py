# bank.py

class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        if balance < 0:
            raise NegativeAmountError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot deposit negative amount.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot withdraw negative amount.")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds.")
        self.balance -= amount
        return self.balance

    def transfer_to(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)
