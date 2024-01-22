import unittest

import exercise


class Price23VatTestCase(unittest.TestCase):
    def test_creating_instance(self):
        p = exercise.Price23Vat(123)

    def test_reading(self):
        p = exercise.Price23Vat(123)
        self.assertAlmostEqual(p.net, 100)
        self.assertEqual(p.pretax, 123)
        self.assertAlmostEqual(p.tax, 23)

    def test_setting_net(self):
        p = exercise.Price23Vat(123)
        p.net = 200
        self.assertEqual(p.net, 200)
        self.assertAlmostEqual(p.pretax, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_pretax(self):
        p = exercise.Price23Vat(123)
        p.pretax = 246
        self.assertAlmostEqual(p.net, 200)
        self.assertEqual(p.pretax, 246)
        self.assertAlmostEqual(p.tax, 46)

    def test_setting_tax(self):
        p = exercise.Price23Vat(123)
        p.tax = 46
        self.assertAlmostEqual(p.net, 200)
        self.assertAlmostEqual(p.pretax, 246)
        self.assertEqual(p.tax, 46)
