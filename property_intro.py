# property
class Account:
    def __init__(self, account_number):
        self.number = account_number
        self._cash = 0

    def print_info(self):
        return self._cash

    # getter
    def get_cash(self):
        return self._cash

    # setter
    def set_cash(self, new_amount):
        if type(new_amount) in [int, float] and new_amount > 0:
            self._cash = new_amount

    # property cash
    cash = property(get_cash, set_cash)


a = Account(12345677356)
print(a.cash)
a.cash = "ala ma kota"
print(a.cash)

# print(a.get_cash)
# a.set_cash(100)
# print(a.get_cash())