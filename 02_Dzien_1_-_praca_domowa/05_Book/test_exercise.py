import unittest

import exercise


class BookTestCase(unittest.TestCase):
    def test_class_Book_is_present(self):
        self.assertTrue(exercise.Book)

    def test_class_Book_has_check_isbn_method(self):
        self.assertTrue(exercise.Book.check_isbn)

    def test_check_isbn_returns_True_for_valid_10_digit_separated_ISBNs(self):
        self.assertTrue(exercise.Book.check_isbn('1-393-16093-X'))
        self.assertTrue(exercise.Book.check_isbn('1-541-14913-0'))
        self.assertTrue(exercise.Book.check_isbn('1-539-56774-5'))
        self.assertTrue(exercise.Book.check_isbn('0-996-06283-1'))

    def test_check_isbn_returns_True_for_valid_10_digit_ISBNs(self):
        self.assertTrue(exercise.Book.check_isbn('139316093X'))
        self.assertTrue(exercise.Book.check_isbn('1541149130'))
        self.assertTrue(exercise.Book.check_isbn('1539567745'))
        self.assertTrue(exercise.Book.check_isbn('0996062831'))

    def test_check_isbn_returns_True_for_valid_13_digit_separated_ISBNs(self):
        self.assertTrue(exercise.Book.check_isbn('978-1-393-16093-9'))
        self.assertTrue(exercise.Book.check_isbn('978-1-593-27966-0'))
        self.assertTrue(exercise.Book.check_isbn('978-1-119-78760-0'))
        self.assertTrue(exercise.Book.check_isbn('978-1-491-91953-8'))

    def test_check_isbn_returns_True_for_valid_13_digit_ISBNs(self):
        self.assertTrue(exercise.Book.check_isbn('9781393160939'))
        self.assertTrue(exercise.Book.check_isbn('9781593279660'))
        self.assertTrue(exercise.Book.check_isbn('9781119787600'))
        self.assertTrue(exercise.Book.check_isbn('9781491919538'))

    def test_check_isbn_returns_False_for_invalid_10_digit_separated_ISBNs(self):
        self.assertFalse(exercise.Book.check_isbn('1-393-16093-8'))
        self.assertFalse(exercise.Book.check_isbn('1-541-14913-3'))
        self.assertFalse(exercise.Book.check_isbn('1-539-56974-5'))
        self.assertFalse(exercise.Book.check_isbn('0-996-06281-1'))

    def test_check_isbn_returns_False_for_invalid_10_digit_ISBNs(self):
        self.assertFalse(exercise.Book.check_isbn('239316093X'))
        self.assertFalse(exercise.Book.check_isbn('1641149130'))
        self.assertFalse(exercise.Book.check_isbn('1549567745'))
        self.assertFalse(exercise.Book.check_isbn('0998062831'))

    def test_check_isbn_returns_False_for_invalid_13_digit_separated_ISBNs(self):
        self.assertFalse(exercise.Book.check_isbn('978-1-393-16093-0'))
        self.assertFalse(exercise.Book.check_isbn('978-1-593-27961-0'))
        self.assertFalse(exercise.Book.check_isbn('978-1-119-78720-0'))
        self.assertFalse(exercise.Book.check_isbn('978-1-491-91353-8'))

    def test_check_isbn_returns_False_for_invalid_13_digit_ISBNs(self):
        self.assertFalse(exercise.Book.check_isbn('9781383160939'))
        self.assertFalse(exercise.Book.check_isbn('9781583279660'))
        self.assertFalse(exercise.Book.check_isbn('9781109787600'))
        self.assertFalse(exercise.Book.check_isbn('9781481919538'))

    def test_check_isbn_returns_False_for_wrong_length_ISBNs(self):
        self.assertFalse(exercise.Book.check_isbn('978139316093'))
        self.assertFalse(exercise.Book.check_isbn('97813931609399'))
        self.assertFalse(exercise.Book.check_isbn('978-1-593-2766-0'))
        self.assertFalse(exercise.Book.check_isbn('978-1-593-27966-00'))

    def test_class_Book_stores_arguments_as_attributes(self):
        book = exercise.Book('Test Title', 'Test Author', '978-1-393-16093-9')
        self.assertEqual(book.title, 'Test Title')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.isbn, '978-1-393-16093-9')

    def test_init_raises_on_invalid_isbn(self):
        with self.assertRaises(ValueError):
            exercise.Book('Test Title', 'Test Author', '978-1-393-16090-9')
