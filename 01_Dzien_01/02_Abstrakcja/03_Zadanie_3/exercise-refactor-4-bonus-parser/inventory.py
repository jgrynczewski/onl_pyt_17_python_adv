import json


class Inventory:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        """Load all book data from a file specified during initialization.

        :returns: {<isbn as string>: {'title': str, 'authors': str, 'price': float, 'amount': int}}
        """
        with open(self.filename, 'r') as f:
            return json.loads(f.read())

    def save(self, content):
        """Saves provided data to a file specified during initialization.

        :param content: {<isbn as string>: {'title': str, 'authors': str, 'price': float, 'amount': int}}
        """
        with open(self.filename, 'w') as f:
            return f.write(json.dumps(content))

    def add_new_book(self, isbn, title, authors, price):
        """Adds new book to the inventory.

        :param str isbn: Book's ISBN
        :param str title: Book's title
        :param str authors: Book's authors
        :param float price: Book's price
        """
        content = self.load()
        content[isbn] = {'title': title, 'authors': authors, 'price': price, 'amount': 0}
        self.save(content)

    def _change_amount(self, isbn, to_add):
        """Changes the available amount of a book by adding `to_add`.
        For internal use only, outside this class you should use `add_books` or `remove_books`.

        :param str isbn: Book's ISBN
        :param int to_add: Amount of books to be added to the inventory. Can be negative.
        :returns: True on success, False if the book was not found.
        """
        try:
            content = self.load()
            content[isbn]['amount'] += to_add
            self.save(content)
            return True
        except KeyError:
            return False

    def add_books(self, isbn, to_add):
        """Adds given amount of books to the inventory.

        :param str isbn: Book's ISBN
        :param int to_add: Amount of books to be added to the inventory.
        :returns: True on success, False if the book was not found.
        """
        return self._change_amount(isbn, to_add=to_add)

    def remove_books(self, isbn, to_remove):
        """Removes given amount of books from the inventory.

        :param str isbn: Book's ISBN
        :param int to_remove: Amount of books to be removed from the inventory.
        :returns: True on success, False if the book was not found.
        """
        return self._change_amount(isbn, to_add=-to_remove)

    def get_book_info(self, isbn):
        """Reads book's info from the inventory.

        :param str isbn: Book's ISBN
        :returns: {'title': str, 'authors': str, 'price': float, 'amount': int} or None, if not found.
        """
        content = self.load()
        try:
            return content[isbn]
        except KeyError:
            return None
