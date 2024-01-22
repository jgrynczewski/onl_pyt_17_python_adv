import unittest

import exercise


class PriceTestCase(unittest.TestCase):
    def test_class_Price_is_present(self):
        self.assertTrue(exercise.Price)

    def test_class_Price_accepts_one_argument_and_stores_it_as_value_attr(self):
        price = exercise.Price(123.45)
        self.assertEqual(price.value, 123.45)

    def test_class_Price_rounds_the_argument(self):
        price = exercise.Price(123.459)
        self.assertEqual(price.value, 123.46)

    def test_class_Price_converts_the_argument_to_float(self):
        price = exercise.Price(123)
        self.assertIsInstance(price.value, float)

    def test_class_Price_created_from_USD(self):
        price_one = exercise.Price.from_usd(50)
        self.assertEqual(price_one.value, 190)

        price_two = exercise.Price.from_usd(150)
        self.assertEqual(price_two.value, 570)

    def test_class_Price_created_from_EUR(self):
        price_one = exercise.Price.from_eur(160)
        self.assertEqual(price_one.value, 720)

        price_two = exercise.Price.from_eur(320)
        self.assertEqual(price_two.value, 1440)

    def test_str_method(self):
        price_one = exercise.Price(10)
        self.assertEqual(str(price_one), '10.0 PLN')

        price_two = exercise.Price(199.99)
        self.assertEqual(str(price_two), '199.99 PLN')
