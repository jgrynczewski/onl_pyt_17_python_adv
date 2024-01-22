import unittest

import exercise


class CartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Cart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Cart()
        c.add(10, 'Potato')
        self.assertCountEqual(c.products, [(10, 'Potato')])
        c.add(30, 'Tomato')
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato')])

    def test_summary(self):
        c = exercise.Cart()
        c.add(10, 'Potato')
        c.add(30, 'Tomato')
        self.assertCountEqual(c.summary(), [(10, 'Potato'), (30, 'Tomato')])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Cart()
        c.add(10, 'Potato')
        c.add(30, 'Tomato')
        c.summary()
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato')])


class Discount20PercentCartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Discount20PercentCart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Discount20PercentCart()
        c.add(10, 'Potato')
        self.assertCountEqual(c.products, [(10, 'Potato')])
        c.add(30, 'Tomato')
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato')])

    def test_summary(self):
        c = exercise.Discount20PercentCart()
        c.add(10, 'Potato')
        c.add(30, 'Tomato')
        self.assertCountEqual(c.summary(), [(8, 'Potato'), (24, 'Tomato')])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Discount20PercentCart()
        c.add(10, 'Potato')
        c.add(30, 'Tomato')
        c.summary()
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato')])


class Above3ProductsCheapestFreeCartTestCase(unittest.TestCase):
    def test_instance_has_products_attribute(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        self.assertCountEqual(c.products, [])

    def test_adding_product(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add(10, 'Potato')
        self.assertCountEqual(c.products, [(10, 'Potato')])
        c.add(30, 'Tomato')
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato')])
        c.add(50, 'Beer')
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato'), (50, 'Beer')])

    def test_summary(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add(10, 'Potato')
        c.add(30, 'Tomato')
        c.add(50, 'Beer')
        self.assertCountEqual(c.summary(), [(10, 'Potato'), (30, 'Tomato'), (50, 'Beer')])
        c.add(15, 'Bread')
        self.assertCountEqual(c.summary(), [(0, 'Potato'), (30, 'Tomato'), (50, 'Beer'), (15, 'Bread')])

    def test_summary_does_not_modify_original_list(self):
        c = exercise.Above3ProductsCheapestFreeCart()
        c.add(10, 'Potato')
        c.add(50, 'Beer')
        c.add(30, 'Tomato')
        c.add(15, 'Bread')
        c.summary()
        self.assertCountEqual(c.products, [(10, 'Potato'), (30, 'Tomato'), (50, 'Beer'), (15, 'Bread')])
