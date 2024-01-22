![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Zadanie 1

W pliku `exercise.py` znajdziesz aplikację, która symuluje grę na giełdzie.

Aplikacja w pętli pokazuje stan Twojego portfela (złotówki oraz dolary amerykańskie), oraz kurs PLN/USD, oraz pyta o decyzję. Możliwe decyzje to:
- `buy` - (kup) wtedy wszystkie złotówki zostaną poświęcone na zakup dolarów
- `sell` - (sprzedaj) wtedy wszystkie dolary zostaną sprzedane
- `wait` (czekaj) lub **pusty string** - nic nie rób, zaczekaj na zmianę kursu

Kod zalicza wszystkie testy automatyczne, ale mimo to jest bardzo niechlujnie napisany. Twoim zadaniem jest wybranie jego fragmentów (podzadań) oraz napisanie klas, które rozwiążą dane podzadanie kompleksowo, oraz użycie tych klas w miejscu oryginalnego kodu. Po zakończonym refaktorze testy automatyczne powinny nadal przechodzić.

Zwróć uwagę, że testy wymagają aby w pliku `exercise.py` istniała funkcja `main(usdpln_rates)`, oraz aby do komunikacji z użytkownikiem były używane `input(...)` oraz `print(...)`. Wszystkie komunikaty powinny pozostać takie same.

## Klasa do napisania: `CommandPrompt`

Napisz klasę, która zajmie się pytaniem o decyzję.

Metoda `__init__` powinna przyjmować trzy argumenty:
- listę/tuplę stringów poprawnych dla komendy **buy**
- listę/tuplę stringów poprawnych dla komendy **sell**
- listę/tuplę stringów poprawnych dla komendy **wait**

Metoda `ask(self)` powinna pytać użytkownika o decyzję, i zwracać tylko jeden z trzech stringów: `"buy"`, `"sell"` albo `"wait"`. Jeśli użytkownik poda coś spoza list przekazanych do `__init__`, powinna wyświetlić komunikat `Invalid choice: <TUTAJ TO CO WPISAŁ UŻYTKOWNIK>` i zapytać ponownie.

Utwórz instancję tej klasy **ponad funkcją** `main(usdpln_rates)`, a w funkcji używaj jej metody `ask()`. Przy tworzeniu instancji podaj takie dane (tuple stringów), aby program działał tak samo jak przed zmianami.

## Klasa do napisania: `Wallet`

Napisz klasę, która zajmie się przechowywaniem walut.

Metoda `__init__` powinna przyjmować 2 argumenty: początkową ilość złotówek i początkową ilość dolarów. Zanim zapiszesz te dwie wartości w instancji, upewnij się, że są typu `float`.

Napisz metody `convert_pln_to_usd(self, usdpln_rate)` oraz `convert_usd_to_pln(self, usdpln_rate)`. Każda z nich powinna wziąć odpowiednio wszystkie dostępne złotówki albo dolary, i przeliczyć je na dolary lub złotówki, po podanym kursie.

Utwórz instancję tej klasy **na początku funkcji** `main(usdpln_rates)`, a w funkcji używaj jej metod i atrybutów. Przy tworzeniu instancji podaj takie dane (początkowe liczby złotówek i dolarów), aby program działał tak samo jak przed zmianami.


# Zadanie 2

## Funkcja `middle_elements`

W pliku `exercise.py` napisz funkcję `middle_elements(sequences)`, która z każdej sekwencji (listy, tupli, etc.) na liście `sequences` wyciągnie środkowy element, a następnie zwróci listę złożoną tylko ze środkowych elementów.

Użyj `len(...)` aby sprawdzić długość sekwencji oraz obliczyć indeks jej środkowego elementu, oraz nawiasów kwadratowych aby ten element pobrać.

Użyj polecenia `python -m unittest` (lub `python3 -m unittest`) aby uruchomić testy automatyczne dla tego zadania.

Jeśli jakaś sekwencja zawiera parzystą liczbę elementów, wybierz prawy z dwóch środkowych. Jeśli jakaś sekwencja jest pusta - pomiń ją.

Przykład:

```python
>>> print(middle_elements(
...  [
...    [6, 7, 8, 9, 10],  # środkowy element to 8
...    ["Kto", "to", "taki?"],  # środkowy element to "to"
...    [],  # pusto - pomijamy
...
...    # środkowe elementy to "siedem" oraz "osiem" - wybieramy "osiem"
...    ["sześć", "siedem", "osiem", "dziewięć"],
...  ]
...))
[8, "to", "osiem"]
```

## Klasa `SequenceOfNumbers`

Następnie napisz klasę `SequenceOfNumbers`. Klasa będzie w stanie reprezentować dowolnie długi ciąg liczb, pamiętając tylko 3 liczby potrzebne do zdefiniowania tego ciągu.

Niech jej metoda `__init__` przyjmuje trzy argumenty: `start`, `stop` oraz `step`. Ta klasa ma reprezentować sekwencję liczb od `start` do `stop` (bez `stop`), z odstępem `step` pomiędzy kolejnymi liczbami.

Przykład: `SequenceOfNumbers(14, 46, 4)` będzie reprezentować następujący ciąg liczb:

```bash
Indeksy:    0       1       2       3       4       5       6      7
Elementy:  14      18      22      26      30      34      38      42   # 46
           ^start                              stop nie jest częścią ciągu^

Długość: 8
```

## Magiczna metoda `__len__`

Dopisz do klasy metodę `__len__`, która na podstawie `start`, `stop` i `step` obliczy długość ciągu.

Dzięki tej metodzie, wbudowana w Pythona funkcja `len()` będzie umiała porozumieć się z klasą `SequenceOfNumbers`.

```python
>>> nums = SequenceOfNumbers(14, 46, 4)
>>> len(nums)
8
```

## Magiczna metoda `__getitem__`

Dopisz do klasy metodę `__getitem__`, która (oprócz `self`) przyjmie argument `index`, oraz zwróci liczbę znajdującą się na miejscu o numerze `index` w ciągu.
Jeśli użytkownik podał zbyt duży lub ujemny `index`, rzuć wyjątek `IndexError` z odpowiednim komentarzem.

Ta metoda jest potrzebna, aby móc odpytywać `SequenceOfNumbers` o jej kolejne elementy, tak jakby to była lista lub tupla - za pomocą nawiasów kwadratowych.

```python
>>> nums = SequenceOfNumbers(14, 46, 4)
>>> nums[0]
14

>>> nums[7]
42

>>> nums[2]
22

>>> nums[-1]
Traceback (most recent call last):
...
IndexError: 'Negative indexes are not supported, sorry!'

>>> nums[8]
Traceback (most recent call last):
...
IndexError: 'Always look beyond the horizon, but never beyond the end of sequence!'
```

## SequenceOfNumbers ma teraz interfejs wymagany przez `middle_elements`

Użyj funkcji `middle_elements`, a jako jej argument przekaż listę złożoną z list, tupli oraz obiektu `SequenceOfNumbers`. Jeśli wszystko poszło zgodnie z planem, `middle_elements` wyciągnie środkową liczbę z obiektu `SequenceOfNumbers`.

### Podpowiedź:
Dla **p** - początek, **k** - koniec, **r** - różnica, **ceil(...)** - zaokrąglenie w górę:

Długość ciągu: `ceil((k - p) / r)`

i-ty element: `p + i * r`


# Zadanie 3

W pliku `app.py` znajdziesz skrypt, który pomaga w zarządzaniu małą księgarnią. Zajmuje się aktualizacją stanu magazynowego, pobieraniem z Google Books informacji o książkach wprowadzanych do oferty, oraz drukowaniem naklejki z ceną i kodem kreskowym.

Przykłady użycia:
```bash
# dodaj książkę o podanym ISBN, w cenie 12.50
python app.py import 9781573561075 12.50

 # dodaj 7 książek do stanu magazynowego
python app.py add 9781573561075 7

 # odejmij 2 książki od stanu magazynowego
python app.py remove 9781573561075 2

# wydrukuj naklejkę z ceną i kodem kreskowym
python app.py print-price-sticker 9781573561075
```

Twoim zadaniem jest uporządkowanie kodu:
- podziel zadanie ("problem") na mniejsze
- wybierz jeden z nich
- napisz klasę która jeden z tych problemów rozwiązuje w całości - najlepiej w osobnym pliku
- usuń wcześniejsze rozwiązanie w kodzie - zastąp je użyciem swojej klasy
- powtarzaj wszystkie kroki, aż kod będzie czytelny i łatwy do zrozumienia

Podpowiedź - fragmenty które zasługują na własną klasę, to m.in:
- odpytywanie Google Books o szczegóły książki
- obsługa stanu magazynowego, z metodami do:
  - zapamiętania informacji o książce
  - dodania do magazynu pewnej liczby danej książki
  - usunięcia z magazynu pewnej liczby danej książki
  - odczytania informacji o książce
- generowanie naklejki z ceną

**Dodatkowo** możesz skorzystać z [parsera](https://docs.python.org/3/library/argparse.html) aby odczytać potrzebne dane.


# Zadanie 4

Zadanie polega na stworzeniu kwestionariusza. Do napisania będzie klasa `Questionnaire` która zbierze wszystkie pytania, oraz klasa `SingleChoiceQuestion` która zajmie się wyświetleniem konkretnego pytania i pobraniem odpowiedzi od użytkownika.

Jeśli chcesz, spróbuj dopisać inne klasy pytań, np. pytanie wielokrotnego wyboru lub pytanie otwarte.

## Klasa `SingleChoiceQuestion`

Napisz klasę `SingleChoiceQuestion`. Jej metoda `__init__` powinna przyjmować dwa argumenty:
- treść pytania (typu string)
- listę odpowiedzi (lista/tupla stringów)

Napisz metodę `ask(self)`, która:
- wyświetli pytanie
- wyświetli odpowiedzi: każda w osobnej linii, poprzedzone kolejnymi literami alfabetu - jak w przykładzie na końcu treści zadania
- zapyta użytkownika o odpowiedź (dozwolone są tylko litery przypisane do dostępnych opcji: dla pytania z trzema odpowiedziami do wyboru, poprawne wybory to `"a"`, `"b"` lub `"c"`)
- wyświetli pustą linię
- zwróci odpowiedź

## Klasa `Questionnaire`

Napisz klasę `Questionnaire`. Jej metoda `__init__` powinna przyjmować jeden argument: tytuł.

Dodaj metodę `add_question(self, question)`, która dopisze pytanie (czyli obiekt klasy `SingleChoiceQuestion`) do listy pytań. W metodzie `__init__` zadbaj o to, aby każda instancja klasy `Questionnaire` miała taką listę, początkowo pustą.

Dodaj metodę `run()`, która:
- wyświetli tytuł ankiety oraz jedną, pustą linię,
- dla każdego pytania (obiektu klasy `SingleChoiceQuestion`) uruchomi jego metodę `ask()`,
- wyświetli napis `'Dziękuję!'`
- zwróci słownik, w którym kluczami będą numery pytań (numerowane od zera), a wartościami wyniki działania metod `ask()` na obiektach pytań.

## Oczekiwany wynik

```python
>>> questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
>>> q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
>>> q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
>>> q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
>>> questionnaire.add_question(q1)
>>> questionnaire.add_question(q2)
>>> questionnaire.add_question(q3)
>>> answers = questionnaire.run()
Ankieta dotycząca zadowolenia z wyboru laptopa

Matryca
a) mniej niż 15 cali
b) od 15 do 17 cali
c) więcej niż 17 cali
Odpowiedź: c  # tutaj skrypt czeka na odpowiedź. Odpowiadamy "c"

Rodzaj ekranu
a) matowy
b) błyszczący
Odpowiedź: c # tutaj skrypt czeka. Odpowiadamy (niepoprawnie) "c"
Niepoprawna odpowiedź, spróbuj ponownie: a # tym razem odpowiemy dobrze: "a"

Czy polecisz go znajomemu?
a) zdecydowanie tak
b) raczej tak
c) nie mam zdania
d) raczej nie
e) zdecydowanie nie
Odpowiedź: b # tutaj skrypt czeka. Odpowiadamy "b"

Dziękuję!
>>> print(answers)
{0: 'c', 1: 'a', 2: 'b'}
```

Podpowiedź:

`chr(97)` to `"a"`, `chr(98)` to `"b"`, `chr(99)` to `"c"`...

`ord("a")` to `97`, `ord("b")` to `98`, `ord("c")` to `99`...
