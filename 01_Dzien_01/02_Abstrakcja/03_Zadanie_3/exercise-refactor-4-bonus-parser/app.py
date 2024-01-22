import sys
import argparse

from googlebooks import GoogleBooksAPI
from inventory import Inventory
from stickerprinter import StickerPrinter


google_books_api = GoogleBooksAPI()
inventory = Inventory('books.json')
stickerprinter = StickerPrinter()

parser = argparse.ArgumentParser(description="Bookseller's Assistant")
parser.add_argument(
    'command',
    metavar='COMMAND',
    type=str,
    choices=['import', 'add', 'remove', 'print-price-sticker'],
    help='Action to do: import / add / remove / print-price-sticker'
)
parser.add_argument('--isbn', type=str, help='ISBN')
parser.add_argument('--amount', type=int, help='Number of books to add/remove')
parser.add_argument('--price', type=float, help='Price of imported book')


def import_book(isbn, price):
    book_info = google_books_api.get_book(isbn)
    if book_info:
        inventory.add_new_book(isbn, book_info['title'], book_info['authors'], price)
    else:
        print('Book not found in Google Books')


def add_books(isbn, amount):
    success = inventory.add_books(isbn, amount)
    if not success:
        print('Book not found in stock')


def remove_books(isbn, amount):
    success = inventory.remove_books(isbn, amount)
    if not success:
        print('Book not found in stock')


def print_price_sticker(isbn):
    book_info = inventory.get_book_info(isbn)
    if book_info:
        stickerprinter.print_price_sticker(isbn, book_info['title'], book_info['price'])
    else:
        print('Book not found in stock')


def main():
    args = parser.parse_args()

    if args.command == 'import':
        if args.isbn is None:
            print('Enter ISBN of imported book')
        elif args.price is None:
            print('Enter price of imported book')
        else:
            import_book(args.isbn, args.price)

    elif args.command == 'add':
        if args.isbn is None:
            print('Enter ISBN to change book stock')
        elif args.amount is None:
            print('Enter number of books to add')
        else:
            add_books(args.isbn, args.amount)

    elif args.command == 'remove':
        if args.isbn is None:
            print('Enter ISBN to change book stock')
        elif args.amount is None:
            print('Enter number of books to remove')
        else:
            remove_books(args.isbn, args.amount)

    elif args.command == 'print-price-sticker':
        if args.isbn is None:
            print('Enter ISBN to print price sticker')
        else:
            print_price_sticker(args.isbn)


if __name__ == '__main__':
    main()
