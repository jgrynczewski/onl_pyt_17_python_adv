![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; zadanie rozwiązywane z wykładowcą
Stwórz klasę `Calculator`. Jej metoda `__init__` ma nie przyjmować żadnych danych.
Każdy nowo stworzony obiekt powinien mieć pustą
listę, w której będzie trzymać historię wywołanych operacji (stwórz ją w `__init__`).
Następnie dodaj do klasy następujące metody:

1. `add(num1, num2)` &ndash; metoda ma dodać do siebie dwie zmienne i zwrócić wynik.
Dodatkowo na liście operacji ma zapamiętać napis: "added `num1` to `num2` got `result`".
2. `multiply(num1, num2)` &ndash; metoda ma pomnożyć przez siebie dwie zmienne i zwrócić wynik. 
Dodatkowo na liście operacji ma zapamiętać napis: "multiplied `num1` with `num2` got `result`".
5. `print_operations()` &ndash; metoda ma wypisać wszystkie zapamiętane operacje.

Pamiętaj o używaniu `self` w odpowiednich miejscach.
Stwórz kilka kalkulatorów i przetestuj ich działanie.


## Zadanie 2
Stwórz klasę `Shape`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
`x`, `y` (określające środek tego kształtu) i `color`.
2. Mieć metodę `describe`, wypisującą informacje o tym kształcie.
3. Mieć metodę `distance`, zwracającą odległość od środków tego oraz innego kształtu;
niech metoda przyjmuje jako parametr inny obiekt klasy `Shape` i liczy odległość od środków obu figur
(jak? przypomnij sobie twierdzenie Pitagorasa).
4. Mieć nadpisaną metodę `__str__` tak, aby po rzutowaniu obiektu do napisu program zwracał:
"Figura koloru *kolor* o środku w punkcie (*x*, *y*)".


## Zadanie 3
Stwórz klasę `BankAccount`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
 * `number` - atrybut ten powinien trzymać numer identyfikacyjny konta (dla uproszczenia możemy założyć,
że numerem konta może być dowolna liczba całkowita),
 * `cash` - atrybut określający ilość pieniędzy na koncie. Ma to być liczba zmiennoprzecinkowa.
2. Posiadać metodę `__init__` przyjmującą tylko numer konta. Atrybut `cash` powinien być zawsze nastawiany na 0.0
dla nowo tworzonego konta.
3. Posiadać metodę `deposit_cash(amount)`, której rolą będzie zwiększenie wartości atrybutu `cash` o podaną watość.
Pamiętaj o sprawdzeniu, czy podana wartość jest większa od 0.0.
4. Posiadać metodę `withdraw_cash(amount)`, której rolą będzie zmniejszenie wartości atrybutu `cash` o podaną watość.
Metoda ta powinna zwracać ilość wypłaconych pieniędzy. Dla uproszczenia zakładamy, że ilośc pieniędzy na koncie
nie może zejść poniżej 0.0. Np. jeżeli z konta, na którym jest 300zł próbujemy wypłacić 500zł, to metoda zwróci nam
tylko 300zł. Pamiętaj o sprawdzeniu, czy podana wartość jest większa od 0.0.
5. Posiadać metodę `print_info()` nie przyjmującą żadnych parametrów.
Metoda ta ma wyświetlić informację o numerze konta i jego stanie.


## Zadanie 4
Stwórz klasę `Employee`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
 * `id` - atrybut ten powinien trzymać numer identyfikacyjny pracownika,
 * `first_name` - atrybut określający imię pracownika,
 * `last_name` - atrybut określający nazwisko pracownika,
 * `_salary` - atrybut określający ile pracownik zarabia za godzinę. Zwróć uwagę na podkreślenie, które mówi,
że atrybut ten nie powinien być dostępny poza klasą.
2. Posiadać metodę `__init__` przyjmującą id, imię i nazwisko.
3. Posiadać metodę `set_salary(salary)`, której rolą będzie ustawienie wartości atrybutu `salary`.
Pamiętaj o sprawdzeniu, czy podana wartość jest:
 * wartością numeryczną,
 * większa od (lub równa) 0.0.

**Podpowiedź:**  
Jeśli chcesz sprawdzić typ zmiennej, użyj funkcji `isinstance()`: [https://docs.python.org/3/library/functions.html#isinstance](https://docs.python.org/3/library/functions.html#isinstance)
