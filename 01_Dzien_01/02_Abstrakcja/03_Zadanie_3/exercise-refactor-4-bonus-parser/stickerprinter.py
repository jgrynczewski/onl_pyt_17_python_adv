import webbrowser
import textwrap
import tempfile
import os

class StickerPrinter:
    def print_price_sticker(self, isbn, title, price):
        """Launches webbrowser and makes it print a price tag.

        :param str isbn: Book's ISBN
        :param str title: Book's title
        :param float price: Book's price
        """
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as price_sticker_file:
            price_sticker_file.write(self._get_html_content(isbn, title, price))
        webbrowser.open(os.path.realpath(price_sticker_file.name))

    def _get_html_content(self, isbn, title, price):
        """Generates the HTML of the sticker.

        :param str isbn: Book's ISBN
        :param str title: Book's title
        :param float price: Book's price
        """
        return textwrap.dedent(f'''
            <!DOCTYPE html>
            <html>
            <head>
            <link href='https://fonts.googleapis.com/css?family=Libre Barcode 39' rel='stylesheet'>
            </head>
            <body>
            <div style="float:left; border: 1px dotted black; padding: 10px; text-align: center">
            <p>{title} - {price} PLN</p>
            <p style="font-family: 'Libre Barcode 39'; font-size: 22px;">{isbn} {price}</p>
            </div>
            <script type="text/javascript">window.print(); window.close();</script>
            </body>
            </html>
        ''')
