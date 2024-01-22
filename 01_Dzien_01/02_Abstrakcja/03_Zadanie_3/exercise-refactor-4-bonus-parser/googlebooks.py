import json
import urllib.request


class GoogleBooksAPI:
    def get_book(self, isbn):
        """Retrieve information about a book.

        :param str isbn: ISBN number of the book
        :returns: {'title': str, 'authors': str} or None
        """
        response = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
        content = json.loads(response.read())
        try:
            book_info = content['items'][0]['volumeInfo']
        except (KeyError, IndexError):
            return None
        return {
                'title': book_info['title'],
                'authors': ', '.join(book_info['authors']),
        }
