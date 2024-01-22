import unittest

import exercise


class Price23VatTestCase(unittest.TestCase):
    def test_creating_instance(self):
        p = exercise.Price23Vat(123)

    def test_reading(self):
        p = exercise.Price23Vat(123)
        self.assertAlmostEqual(p.get_net(), 100)
        self.assertEqual(p.get_pretax(), 123)
        self.assertAlmostEqual(p.get_tax(), 23)

    def test_setting_net(self):
        p = exercise.Price23Vat(123)
        p.set_net(200)
        self.assertEqual(p.get_net(), 200)
        self.assertAlmostEqual(p.get_pretax(), 246)
        self.assertAlmostEqual(p.get_tax(), 46)

    def test_setting_pretax(self):
        p = exercise.Price23Vat(123)
        p.set_pretax(246)
        self.assertAlmostEqual(p.get_net(), 200)
        self.assertEqual(p.get_pretax(), 246)
        self.assertAlmostEqual(p.get_tax(), 46)

    def test_setting_tax(self):
        p = exercise.Price23Vat(123)
        p.set_tax(46)
        self.assertAlmostEqual(p.get_net(), 200)
        self.assertAlmostEqual(p.get_pretax(), 246)
        self.assertEqual(p.get_tax(), 46)
