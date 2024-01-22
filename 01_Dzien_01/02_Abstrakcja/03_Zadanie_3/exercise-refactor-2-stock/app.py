import sys
import tempfile
import webbrowser
import os
import textwrap

from googlebooks import GoogleBooksAPI
from inventory import Inventory


google_books_api = GoogleBooksAPI()
inventory = Inventory('books.json')


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

    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as price_sticker_file:
        price_sticker_file.write(textwrap.dedent(f'''
            <!DOCTYPE html>
            <html>
            <head>
            <link href='https://fonts.googleapis.com/css?family=Libre Barcode 39' rel='stylesheet'>
            </head>
            <body>
            <div style="float:left; border: 1px dotted black; padding: 10px; text-align: center">
            <p>{store_content[isbn]['title']} - {store_content[isbn]['price']} PLN</p>
            <p style="font-family: 'Libre Barcode 39'; font-size: 22px;">{isbn} {store_content[isbn]['price']}</p>
            </div>
            <script type="text/javascript">window.print(); window.close();</script>
            </body>
            </html>
        '''))
        webbrowser.open(os.path.realpath(price_sticker_file.name))
