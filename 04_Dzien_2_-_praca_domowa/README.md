![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1.

### Część 1

Napisz klasę `Product`, która w metodzie `__init__` przyjmie argumenty: `name`, `price` i zapisze je jako atrybuty produktu.

Dodatkowo `__init__` powinno w produkcie ustawiać niepowtarzalny atrybut `id`.

### Część 2

Napisz klasę `ShoppingCart`. Jej metoda `__init__` nie wymaga żadnych atrybutów (oprócz oczywiście `self`).

Metoda `__init__` powinna w instancji koszyka stworzyć:
 - pusty słownik `products` (jako atrybut). Kluczem w tym słowniku będą `id` produktów, a wartością całe produkty (instancje klasy `Product`).
 - pusty słownik `quantities` (jako atrybut). Kluczem będą `id` produktów, a wartością będzie liczba sztuk tego produktu w koszyku.

Klasa powinna mieć też nastepujące metody:

 - `add_product(product)` - metoda ta powinna dodawać nowy produkt do słownika `products` oraz uaktualnić ilość tego produktu w słowniku `quantities`.
 - `remove_product(product)` - metoda ta powinna usuwać produkt z koszyka (weź pod uwagę oba słowniki: `products` i `quantities`). Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
 - `change_product_quantity(product, new_quantity)` - metoda ta powinna zmieniać ilość danego produktu w koszyku. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić. Jeśli `new_quantity` to zero, należy produkt usunąć z koszyka. Podanie ujemnego `new_quantity` powinno skutkować rzuceniem wyjątku `ValueError` z odpowiednim komentarzem.
 - `get_receipt()` - metoda tworząca paragon. Nie powinna sama drukować (używać `print(...)`), zamiast tego powinna zwrócić string. Przykład oczekiwanego paragonu znajdziesz na końcu zadania.

Wszystkie ww. argumenty o nazwie `product` powinny być instancją klasy `Product`.

### Część 3

Zmodyfikuj metodę `get_receipt()` tak, aby nadawała rabat -30% na łączną cenę za dany produkt, jeśli w koszyku są co najmniej 3 sztuki tego produktu.

### Przykład użycia:

```python
>>> bread = Product('Bread', 2.70)
>>> ham = Product('Ham', 8.40)
>>> cheese = Product('Cheese', 4.40)
>>> chive = Product('Chive', 1.50)
>>> pepper = Product('Pepper', 2.35)

>>> print(bread.id)
1
>>> print(pepper.id)
5
>>> print(pepper.name)
'Pepper'
>>> print(pepper.price)
2.35

>>> cart = ShoppingCart()
>>> print(cart.products)
{}
>>> print(cart.quantities)
{}
>>> print(cart.get_receipt())
Suma: 0zł

>>> cart.add_product(bread)
>>> cart.add_product(bread)
>>> cart.add_product(bread)
>>> cart.add_product(pepper)
>>> cart.add_product(chive)
>>> cart.change_product_quantity(pepper, 2)
>>> print(cart.products)
{1: <...Product object...>, 5: <...Product object...>, 4: <...Product object...>}
>>> print(cart.quantities)
{1: 3, 5: 2, 4: 1}

>>> cart.remove_product(bread)
>>> print(cart.get_receipt())
# Order MAY be different
Pepper - amount: 2, price: 2.35zł, total: 4.7zł
Chive - amount: 1, price: 1.5zł, total: 1.5zł

Total: 6.2zł
```


# Zadanie 2

Napisz klasę `Price23Vat`. Jej metoda `__init__` powinna przyjmować jedną wartość: kwotę brutto, i zapisywać ją jako atrybut `_pretax`.

Oprócz tego na podstawie kwoty brutto metoda `__init__` powinna obliczyć i zapisać atrybuty `_net` oraz `_tax`. Przyjmij 23% podatku VAT - tak jak sugeruje nazwa klasy.

Dopisz metody `get_net()`, `get_pretax()` oraz `get_tax()`, które będą zwracały wartości odpowiadających im atrybutów.

Dopisz metody `set_net(value)`, `set_pretax(value)` oraz `set_tax(value)`, które zapamiętają przekazany argument, oraz obliczą i zapamiętają pozostałe dwa.


# Zadanie 3

Do klasy `Square`, którą napisałeś na zajęciach, dopisz gettery i settery dla boku, pola, obwodu i przekątnej, używając `@property`.

Gettery mogą zwracać wartości atrybutów, albo wynik działania odpowiadającym im metod `get_...`.

Settery powinny korzystać z już istniejących metod `set_...`, aby nie powielać kodu.

Przykład:
```python
square = Square(11)

print(square.get_side())  # 11
print(square.side)        # 11
print(square.perimeter)   # 44

square.perimeter = 48

print(square.get_side())  # 12
print(square.side)        # 12
print(square.perimeter)   # 48
```


# Zadanie 4

Napisz klasę `Price23Vat` jeszcze raz, ale **tym razem użyj `@property`** aby stworzyć gettery i settery dla kwot brutto (pretax), netto oraz tax. Pomiń pisanie metod `get_...` i `set_...`.

Przykład:

```python
price = Price23Vat(123)

print(price.pretax)        # 123
print(price.tax)           # 23
print(price.net)           # 100

price.tax = 69

print(price.pretax)        # 369
print(price.tax)           # 69
print(price.net)           # 300
```
