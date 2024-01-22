![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


### Klasa `Cart`

Stwórz klasę `Cart` - będzie reprezentowała koszyk w sklepie internetowym.

W metodzie `__init__` stwórz atrybut `products` - niech na początku będzie pustą listą.

Stwórz metodę `add`, która przyjmie dwa argumenty: cenę (typu `int` lub `float`) oraz nazwę produktu (typu `str`). Metoda ma dopisać tuplę `(cena, nazwa)` na końcu listy w atrybucie `products`.

Stwórz metodę `summary`, która po prostu zwróci wartość atrybutu `products`.

### Klasa `Discount20PercentCart`

Napisz klasę `Discount20PercentCart`, która dziedziczy z klasy `Cart`.

Metoda `summary` klasy `Discount20PercentCart` powinna zwrócić listę tupli (podobnie jak `summary` w klasie `Cart`), ale ceny mają być zmniejszone o 20%.

### Klasa `Above3ProductsCheapestFreeCart`

Napisz klasę `Above3ProductsCheapestFreeCart`, która dziedziczy z `Cart`.

Metoda `summary` klasy `Above3ProductsCheapestFreeCart` powinna zwrócić listę tupli; jeśli na liście są więcej niż 3 produkty, cena najtańszego powinna być zmieniona na zero.

**Do zadania są dołączone testy - możesz je uruchomić poleceniem `python3 -m unittest`.**
