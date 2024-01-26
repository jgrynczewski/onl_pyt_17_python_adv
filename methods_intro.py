class Cow:
    wisdom = 5

    def __init__(self, name):
        self.name = name

    def introduce_yourself(self):
        print(f"Cześć, jest {self.name}")

    @classmethod
    def increase_wisdom(cls):
        cls.wisdom += 2

    @staticmethod
    def evaluate_circle_area(r):
        return 3.14 * r**2


c1 = Cow("Mućka")
c2 = Cow("Milka")

print(c1.wisdom)
print(c2.wisdom)

Cow.increase_wisdom()

print(c1.wisdom)
print(c2.wisdom)

result = c1.evaluate_circle_area(10)
print(result)
