class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount > self.cash:
            withdraw = self.cash
            self.cash = 0
            return withdraw

        self.cash -= amount
        return amount

    def print_info(self):
        print(f"Konta o numerze {self.number} i stanie {self.cash}")


account = BankAccount(1234567890)
account.print_info()

account.deposit_cash(100.0)
account.print_info()

amount = account.withdraw_cash(75.0)
account.print_info()

print(f"dostajemy: {amount}")
print(f"stan konta: {account.cash}")

print("===================")

amount = account.withdraw_cash(75.0)
print(f"dostajemy: {amount}")
print(f"stan konta: {account.cash}")

account.print_info()
