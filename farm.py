# snake case (zmienne, funkcje, moduły i pakiety)
# to_jest_nowa_nazwa_mojej_zmiennej
def func_name():
    pass


# Camel case (klas)
# ToJesteNowaNazwaMojejKlasy
class Cow:
    def __init__(self, name, age=0):
        self.is_alive = True
        self.name = name
        self.age = age
        self.places = []

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

    def append_place(self, place_name):
        self.places.append(place_name)

# ============================
# ============================


first_cow = Cow("mućka", 2)
second_cow = Cow("milka")

first_cow.speak()
second_cow.speak()

for _ in range(100):
    first_cow.get_older()

first_cow.speak()
second_cow.speak()

result = second_cow.get_age()
print(second_cow.places)
second_cow.append_place("Pastwisko nr 3")
second_cow.append_place("Stodola 2")
print(second_cow.places)

print(result)
