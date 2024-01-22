# snake case (zmienne, funkcje, moduły i pakiety)
# to_jest_nowa_nazwa_mojej_zmiennej
def func_name():
    pass


# Camel case (klas)
# ToJesteNowaNazwaMojejKlasy
class Cow:
    def __init__(self, name, age=0):
        self.type = 'mammals'
        self.name = name
        self.age = age

    def speak(self):
        print(f"Muuuuuuuuuuu. Cześć jestem {self.name}")

    def get_older(self):
        self.age += 1

# ============================
# ============================

first_cow = Cow("mućka", 2)
second_cow = Cow("milka")

first_cow.speak()
second_cow.speak()

print(first_cow.age)
first_cow.get_older()
print(first_cow.age)
