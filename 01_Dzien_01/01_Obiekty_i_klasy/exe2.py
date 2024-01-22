class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f"Figura o środku w punkcie ({self.x}, {self.y}) i kolorze {self.color}")

    def distance(self, other_shape):
        return ((self.x - other_shape.x)**2+(self.y - other_shape.y)**2)**0.5

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"


s1 = Shape(0, 0, 'yellow')
s2 = Shape(2, 2, 'black')

s1.describe()
print(s1.distance(s2))
print(s1)
