# polimorfizm - wielopastociowość
class Dog:
    def speak(self):
        print("Hau hau hau")


class Cat:
    def speak(self):
        print("Miau miau miau")


class Horse:
    def speak(self):
        print("Ihaaaaa")


def give_voice(x):
    x.speak()


zoo = [Dog(), Cat(), Horse()]
for animal in zoo:
    give_voice(animal)
