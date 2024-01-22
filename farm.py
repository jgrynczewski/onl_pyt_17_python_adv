# snake case (zmienne, funkcje, moduły i pakiety)
# to_jest_nowa_nazwa_mojej_zmiennej
def func_name():
    pass


# Camel case (klas)
# ToJesteNowaNazwaMojejKlasy
class Cow:
    def __init__(self, name, account, age=0):
        self.is_alive = True
        self.name = name
        self.age = age
        # Kompozycja (ang. composition) (obiekt klasy Cow komponuje się/składa się/ma (HAS-A) obiekt klasy Account)
        self.account = account

    def speak(self):
        if self.is_alive:
            print(f"Muuuuuuuuuuu. Cześć jestem {self.name}")
        else:
            print("RIP")

    def get_older(self):
        if self.is_alive:
            self.age += 1
            if self.age > 10:
                self.is_alive = False

    def get_age(self):
        return self.age

    # Zależność (ang. dependency) (obiekt klasy Cow używa (USE-A) obiektu klasy Place)
    def visit_place(self, place):
        print(f"O jakie piękne miejsce {place.name} ({place.type})")

    def sum_age(self, other_cow):
        result = self.age + other_cow.age
        print(f"Razem mamy {result}")


class Place:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class Account:
    def __init__(self, amount):
        self.amount = amount


# ============================
# ============================

place1 = Place('pastwisko', 'numer 3')
place2 = Place('pastwisko', 'numer 5')
place3 = Place('pastwisko', 'numer 9')

place4 = Place('stodola', 'kwiecista')
place5 = Place('stodola', 'złota')

account1 = Account(100)
account2 = Account(200)

first_cow = Cow("mućka", account1, 2)
second_cow = Cow("milka", account2)

first_cow.speak()
second_cow.speak()

for _ in range(100):
    first_cow.get_older()

first_cow.speak()
second_cow.speak()

result = second_cow.get_age()
print(result)

# powiązania
# Dependency (zależność, relacja typu USE-A - używa)
# Obiekt klasy Cow używa (USE-A) obiektu klasy Place
second_cow.visit_place(place1)
second_cow.visit_place(place5)

second_cow.sum_age(first_cow)
