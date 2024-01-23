# Dziedziczenie (inheritance) - najsilniejszy sposób powiązania ze sobą klas
# Dziedziczenie to realizacja zasady DRY w obiektówce

# DRY - Don't Reapat Yourself
# KISS - Keep It Simple, Stupid
# YAGNI - You Ain't Gonna Need It
class Animal:
    def introduce_yourself(self):
        print(f"Witaj, nazywam się {self.name}")

# Relacja dziedziczenia jest opisywana terminem IS-A
# Cow IS-A Animal (Krowa JEST zwierzęciem)


class Cow(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Muuuuuuuu")

    # 1. Krowa dziedziczy metodę rodzica introduce_yourself


class Horse(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Ihaaaaaa")

    # 2. Koń nadpisuje metodę rodzica introduce_yourself
    def introduce_yourself(self):
        print(f"Witaj, jestem koniem i nazywam się {self.name}")


class Pig(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Chrum chrum chrum")

    # 3. Świnia rozbudowuje metodę rodzica introduce_yourself
    def introduce_yourself(self):
        super().introduce_yourself()
        print("I jestem świnią")


c = Cow("Mućka", 2)
h = Horse("Horacy", 3)
p = Pig("Baby", 1)

c.introduce_yourself()
h.introduce_yourself()
p.introduce_yourself()
