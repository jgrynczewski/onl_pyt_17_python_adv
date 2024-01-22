import unittest

import exercise


class MiddleElementsTestCase(unittest.TestCase):
    def test_middle_elements_of_empty_list_of_sequences(self):
        result = exercise.middle_elements([])
        self.assertEqual(result, [])

    def test_middle_elements_of_one_list(self):
        result = exercise.middle_elements([["Huey", "Dewey", "Louie"]])
        self.assertEqual(result, ["Dewey"])

    def test_middle_elements_of_many_lists(self):
        result = exercise.middle_elements([
            ["Huey", "Dewey", "Louie"],
            ["one", "two", "three"],
        ])
        self.assertEqual(result, ["Dewey", "two"])

    def test_middle_elements_skips_empty_sequences(self):
        result = exercise.middle_elements([
            [],
            ["Huey", "Dewey", "Louie"],
            [],
            ["one", "two", "three"],
            []
        ])
        self.assertEqual(result, ["Dewey", "two"])

    def test_middle_elements_of_many_lists_with_even_number_of_elements(self):
        result = exercise.middle_elements([
            ["Batman", "Robin"],
            ["one", "two", "three", "four"],
            [11, 12, 13, 14, 15, 16],
        ])
        self.assertEqual(result, ["Robin", "three", 14])


class SequenceOfNumbersTestCase(unittest.TestCase):
    def test_init_accepts_three_args(self):
        exercise.SequenceOfNumbers(20, 50, 5)

    def test_returns_proper_length_of_empty_sequence(self):
        self.assertEqual(
            0, len(exercise.SequenceOfNumbers(5, 5, 1))
        )

    def test_returns_proper_length_when_step_is_1(self):
        self.assertEqual(
            10, len(exercise.SequenceOfNumbers(5, 15, 1))
        )

    def test_returns_proper_length_when_step_is_2(self):
        self.assertEqual(
            4, len(exercise.SequenceOfNumbers(5, 13, 2))
        )
        self.assertEqual(
            5, len(exercise.SequenceOfNumbers(5, 14, 2))
        )
        self.assertEqual(
            5, len(exercise.SequenceOfNumbers(5, 15, 2))
        )

    def test_returns_proper_first_element(self):
        sequence = exercise.SequenceOfNumbers(5, 15, 3)
        self.assertEqual(
            5, sequence[0]
        )

    def test_returns_proper_second_element(self):
        sequence = exercise.SequenceOfNumbers(5, 15, 3)
        self.assertEqual(
            8, sequence[1]
        )

    def test_returns_proper_last_element(self):
        sequence = exercise.SequenceOfNumbers(5, 15, 3)
        self.assertEqual(
            14, sequence[3]
        )

    def test_raises_indexerror_with_negative_index(self):
        sequence = exercise.SequenceOfNumbers(5, 15, 3)
        with self.assertRaises(IndexError):
            sequence[-1]

    def test_raises_indexerror_with_too_big_index(self):
        sequence = exercise.SequenceOfNumbers(5, 15, 3)
        with self.assertRaises(IndexError):
            sequence[4]


class MiddleElementsAndSequenceOfNumbers(unittest.TestCase):
    def test_sequenceofnumbers_works_with_middle_elements(self):
        seq1 = exercise.SequenceOfNumbers(0, 0, 1)  # to be skipped
        seq2 = exercise.SequenceOfNumbers(5, 15, 1)  # middle is 10
        seq3 = exercise.SequenceOfNumbers(5, 15, 4)  # middle is 9
        seq4 = exercise.SequenceOfNumbers(100, 201, 1)  # middle is 150
        result = exercise.middle_elements([
            seq1,
            ['one', 'two', 'three'],
            seq2,
            'abcde',
            seq3,
            ('Beam', 'me', 'up,', 'Chewie'),
            seq4
        ])
        self.assertEqual(['two', 10, 'c', 9, 'up,', 150], result)
