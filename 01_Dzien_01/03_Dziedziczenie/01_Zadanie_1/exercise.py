class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        self.products.append(
            (price, name)
        )

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        # Z użyciem list comprehension
        return [(0.8*product[0], product[1]) for product in self.products]

        # Z użyciem pętli
        # result = []
        # for product in self.products:
        #     result.append(
        #         (0.8*product[0], product[1])
        #     )
        # return result


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        sorted_products = sorted(self.products)
        if len(self.products) > 3:
            sorted_products[0] = (0, sorted_products[0][1])

        return sorted_products


# Obie podklasy dziedziczą metody __init__ i add po klasie Cart, a nadpisują metodę summary klasy Cart

c1 = Cart()
c1.add(1, 'lizak')
c1.add(50000, 'bmv')
c1.add(10, 'komiks')
c1.add(80, 'kwiaty')

res = c1.summary()
print(res)

print("===========================")

c2 = Discount20PercentCart()
c2.add(1, 'lizak')
c2.add(50000, 'bmv')
c2.add(10, 'komiks')
c2.add(80, 'kwiaty')

res = c2.summary()
print(res)

print("===========================")

c3 = Above3ProductsCheapestFreeCart()
c3.add(1, 'lizak')
c3.add(50000, 'bmv')
c3.add(10, 'komiks')
c3.add(80, 'kwiaty')

res = c3.summary()
print(res)
