import unittest

import exercise


class SquareTestCase(unittest.TestCase):
    def test_creating_instance(self):
        sq = exercise.Square(4)

    def test_reading_side(self):
        sq = exercise.Square(5)
        self.assertEqual(sq.side, 5)

    def test_reading_area(self):
        sq = exercise.Square(7)
        self.assertEqual(sq.area, 49)

    def test_reading_diagonal(self):
        sq = exercise.Square(8)
        self.assertAlmostEqual(sq.diagonal, (8**2 + 8**2) ** 0.5)

    def test_setting_side(self):
        sq = exercise.Square(100)
        sq.side = 9
        self.assertEqual(sq.side, 9)
        self.assertEqual(sq.area, 81)
        self.assertEqual(sq.diagonal, 162**0.5)

    def test_setting_area(self):
        sq = exercise.Square(100)
        sq.area = 9
        self.assertEqual(sq.side, 3)
        self.assertEqual(sq.area, 9)
        self.assertEqual(sq.diagonal, 18**0.5)

    def test_setting_diagonal(self):
        sq = exercise.Square(100)
        sq.diagonal = 9
        self.assertAlmostEqual(sq.side, 40.5**0.5)
        self.assertAlmostEqual(sq.area, 40.5)
        self.assertEqual(sq.diagonal, 9)
