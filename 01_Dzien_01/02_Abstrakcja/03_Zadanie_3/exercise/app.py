import sys
import json
import tempfile
import urllib.request
import webbrowser
import os
import textwrap


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
    response = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
    content = json.loads(response.read())
    try:
        book_info = content['items'][0]['volumeInfo']
    except (KeyError, IndexError):
        print('Book with this ISBN not found in Google Books')
        sys.exit()
    with open('books.json', 'r') as f:
        store_content = json.loads(f.read())
        store_content[isbn] = {
            'title': book_info['title'],
            'authors': ', '.join(book_info['authors']),
            'amount': 0,
            'price': price,
        }
    with open('books.json', 'w') as f:
        f.write(json.dumps(store_content))
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
    with open('books.json', 'r') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
        print('Book not found in stock')
        sys.exit()
    store_content[isbn]['amount'] += to_add
    with open('books.json', 'w') as f:
        f.write(json.dumps(store_content))
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
    with open('books.json', 'r') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
        print('Book not found in stock')
        sys.exit()
    store_content[isbn]['amount'] -= to_remove
    with open('books.json', 'w') as f:
        f.write(json.dumps(store_content))
if sys.argv[1] == 'print-price-sticker':
    if len(sys.argv) <= 2:
        print('Enter ISBN to print price sticker')
        sys.exit()
    else:
        isbn = sys.argv[2]
    with open('books.json') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
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
