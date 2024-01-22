import unittest

import exercise


class SquareTestCase(unittest.TestCase):
    def test_creating_instance(self):
        sq = exercise.Square(4)

    def test_reading_side(self):
        sq = exercise.Square(5)
        self.assertAlmostEqual(sq.get_side(), 5)

    def test_reading_area(self):
        sq = exercise.Square(7)
        self.assertAlmostEqual(sq.get_area(), 49)

    def test_reading_diagonal(self):
        sq = exercise.Square(8)
        self.assertAlmostEqual(sq.get_diagonal(), (8**2 + 8**2) ** 0.5)

    def test_setting_side(self):
        sq = exercise.Square(100)
        sq.set_side(9)
        self.assertAlmostEqual(sq.get_side(), 9)
        self.assertAlmostEqual(sq.get_area(), 81)
        self.assertAlmostEqual(sq.get_diagonal(), 162**0.5)

    def test_setting_area(self):
        sq = exercise.Square(100)
        sq.set_area(9)
        self.assertAlmostEqual(sq.get_side(), 3)
        self.assertAlmostEqual(sq.get_area(), 9)
        self.assertAlmostEqual(sq.get_diagonal(), 18**0.5)

    def test_setting_diagonal(self):
        sq = exercise.Square(100)
        sq.set_diagonal(9)
        self.assertAlmostEqual(sq.get_side(), 40.5**0.5)
        self.assertAlmostEqual(sq.get_area(), 40.5)
        self.assertAlmostEqual(sq.get_diagonal(), 9)
