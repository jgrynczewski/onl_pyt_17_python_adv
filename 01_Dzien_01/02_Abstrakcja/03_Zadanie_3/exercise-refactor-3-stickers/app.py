import sys

from googlebooks import GoogleBooksAPI
from inventory import Inventory
from stickerprinter import StickerPrinter


google_books_api = GoogleBooksAPI()
inventory = Inventory('books.json')
stickerprinter = StickerPrinter()


if len(sys.argv) <= 1:
    print('Enter command')
    sys.exit()


if sys.argv[1] == 'import':
    if len(sys.argv) <= 2:
        print('Enter ISBN of imported book')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Enter price of imported book')
        sys.exit()
    else:
        isbn = sys.argv[2]
        price = float(sys.argv[3])

    book_info = google_books_api.get_book(isbn)
    if book_info:
        inventory.add_new_book(isbn, book_info['title'], book_info['authors'], price)
    else:
        print('Book not found in Google Books')


if sys.argv[1] == 'add':
    if len(sys.argv) <= 2:
        print('Enter ISBN to change book stock')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Enter number of books to add')
        sys.exit()
    else:
        isbn = sys.argv[2]
        to_add = int(sys.argv[3])

    success = inventory.add_books(isbn, to_add)
    if not success:
        print('Book not found in stock')
        sys.exit()

if sys.argv[1] == 'remove':
    if len(sys.argv) <= 2:
        print('Enter ISBN to change book stock')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Enter number of books to remove')
        sys.exit()
    else:
        isbn = sys.argv[2]
        to_remove = int(sys.argv[3])

    success = inventory.remove_books(isbn, to_remove)
    if not success:
        print('Book not found in stock')
        sys.exit()


if sys.argv[1] == 'print-price-sticker':
    if len(sys.argv) <= 2:
        print('Enter ISBN to print price sticker')
        sys.exit()
    else:
        isbn = sys.argv[2]

    book_info = inventory.get_book_info(isbn)
    if not book_info:
        print('Book not found in stock')
        sys.exit()

    stickerprinter.print_price_sticker(isbn, book_info['title'], book_info['price'])
