![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


Stwórz klasę `Square`. Niech jej metoda `__init__` przyjmuje jeden argument: długość krawędzi, i zapamiętuje je jako atrybut `_side`. Zwróć uwagę na znak `_` na początku nazwy atrybutu!

Cechy kwadratów to m.in.:
- długość krawędzi
- obwód
- pole
- przekątna

Rozbuduj metodę `__init__` - niech na podstawie podanej długości boku **obliczy** obwód, pole i przekątną, i zapamięta te liczby jako `_perimeter`, `_area` i `_diagonal`.

Dopisz metody `get_side()`, `get_perimeter()`, `get_area()` i `get_diagonal()`, które po prostu zwrócą wartości odpowiadających im atrybutów.

Kwadrat powinien mieć możliwość zmiany rozmiaru na kilka sposobów:
- za pomocą podania nowej długości krawędzi,
- za pomocą podania nowego obwodu,
- za pomocą podania nowego pola,
- za pomocą podania nowej przekątnej.

Napisz metody `set_side(new_length)`, `set_perimeter(new_length)`, `set_area(new_area)` oraz `set_diagonal(new_length)`. Każda z nich powinna zapamiętać argument w odpowiadającym jej atrybucie, oraz zaktualizować pozostałe atrybuty, aby instancja `Square` miała spójne dane.

## Dla chętnych

Zadanie posiada testy automatyczne testujące tworzenie instancji, oraz odczyt i zapis długości krawędzi, pola i przekątnej. Przyjrzyj się tym testom, i w podobny sposób dopisz testy:
- `test_reading_perimeter` testujący metodę do odczytu obwodu (wzoruj się na pozostałych testach `test_reading_...`)
- `test_setting_perimeter` testujący metodę do edycji kwadratu na podstawie obwodu
- Zmodyfikuj testy `test_setting_area`, `test_setting_diagonal` i `test_setting_side` tak, aby sprawdzały też obwód.

Jeśli liczba otrzymana w obliczeniach będzie miała cyfry po przecinku, używaj `assertAlmostEqual` zamiast `assertEqual` - komputery nie zawsze radzą sobie z takimi liczbami - sprawdź, jaki wynik daje `0.1 + 0.1 + 0.1`.
