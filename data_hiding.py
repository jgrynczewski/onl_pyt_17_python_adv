# enkapsulacja (aka hermetyzacja, kapsułkowanie)

# modyfikatory dostępu
# cash - składowa (metoda/atrybut) publiczna (śmiało)
# _cash - składowa chroniona (wchodzisz na własną odpowiedzialność) - składowa dostępna wewnątrz klasy i wewnątrz wszystkich klas po niej dziedziczących (tzn. wszystkich jej podklas)
# __cash - składowa prywatna  (wstęp wzbroniony) - składowa dostępna tylko wewnątrz klasy

class Account:
    def __init__(self, account_number):
        self.number = account_number
        self.__cash = 0  # atrybut prywatny

    def print_info(self):
        return self.__cash

    # getter
    def get_cash(self):
        return self.__cash

    # setter
    def set_cash(self, new_amount):
        if type(new_amount) in [int, float] and new_amount > 0:
            self.__cash = new_amount
