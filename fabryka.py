class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # metoda fabrykująca
    @classmethod
    def create_porche(cls, model):
        return cls("Porche", model)


c = Car("BMV", "Serie 3")

c2 = Car.create_porche(911)
print(c2.brand)
