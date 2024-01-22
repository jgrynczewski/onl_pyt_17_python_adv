# enkapsulacja (aka hermetyzacja, kapsułkowanie)

# modyfikatory dostępu
# cash - składowa (metoda/atrybut) publiczna (śmiało)
# _cash - składowa chroniona (wchodzisz na własną odpowiedzialność)
# __cash - składowa prywatna  (wstęp wzbroniony)

class Account:
    def __init__(self, account_number):
        self.number = account_number
        self.__cash = 0  # atrybut prywatny

    def print_info(self):
        return self.__cash


a1 = Account(555666777888)
res = a1.print_info()
print(res)
