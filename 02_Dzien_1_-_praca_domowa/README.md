![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Zadanie 1

Zadanie polega na napisaniu zestawu klas, które pozwolą zamodelować składniki jedzenia, posiłki i plan dnia, oraz pozwolą w łatwy sposób obliczyć ile białka, węglowodanów, tłuszczy oraz kilokalorii dostarczą posiłki w ramach danego planu.

## Składnik

Napisz klasę, która będzie reprezentowała składnik posiłku. Jej metoda `__init__` powinna przyjmować:
- nazwę (`str`)
- ilość białka w 100g produktu (`float` lub `int`)
- ilość węglowodanów w 100g produktu (`float` lub `int`)
- ilość tłuszczy w 100g produktu (`float` lub `int`)

## Posiłek

Napisz klasę, która będzie reprezentowała posiłki. Jej metoda `__init__` powinna przyjmować jeden argument - nazwę posiłku.

Dopisz do niej metodę, która pozwoli na dodawanie określonej ilości składników (w gramach).

## Plan dnia

Napisz klasę, która będzie reprezentowała plan dnia. Powinna mieć metodę służącą do dodawania kolejnych posiłków, oraz metodę drukującą podsumowanie, jak w przykładzie poniżej.

```
# Uwaga, pseudokod!

egg = Utwórz Składnik Jajko: białko = 13, węglowodany = 1.1, tłuszcze = 11
tomato = Utwórz Składnik Pomidor: białko = 0.9, węglowodany = 3.9, tłuszcze = 0.2
bread = Utwórz Składnik Chleb: białko = 9, węglowodany = 49, tłuszcze = 3.2

scrambled_eggs = Utwórz Posiłek Jajecznica
dodaj 200g egg do scrambled_eggs
dodaj 50g tomato do scrambled_eggs

sandwich = Utwórz Posiłek Kanapka
dodaj 25g bread do sandwich
dodaj 50g tomato do sandwich

very_minimalistic_menu = Utwórz Plan Oszczędny
dodaj scrambled_eggs do very_minimalistic_menu
dodaj sandwich do very_minimalistic_menu

wyświetl podsumowanie very_minimalistic_menu
```
Wynik (podsumowanie planu "Oszczędnego"):
```
Oszczędny

Posiłek: Jajecznica
- 200g Jajko (26g białka, 2.2g węglowodanów, 22g tłuszczy, 310.8 kcal)
- 50g Pomidor (0.45g białka, 1.95g węglowodanów, 0.1g tłuszczy, 10.5 kcal)
Razem: 26.45g białka, 4.15g węglowodanów, 22.1g tłuszczy, 321.3 kcal

Posiłek: Kanapka
- 25g Chleb (2.25g białka, 12.25g węglowodanów, 0.8g tłuszczy, 65.2 kcal)
- 50g Pomidor (0.45g białka, 1.95g węglowodanów, 0.1g tłuszczy, 10.5 kcal)
Razem: 2.7g białka, 14.2g węglowodanów, 0.9g tłuszczy, 75.7 kcal

RAZEM: 29.15g białka, 18.35g węglowodanów, 23g tłuszczy, 397 kcal
```

## Kalorie

Kalorie danego składnika są obliczane ze wzoru:
```
kcal = białko * 4 + węglowodany * 4 + tłuszcze * 9.4
```


# Zadanie 2

Napisz klasę `Price`, która w metodzie `__init__` przyjmie liczbę (`int` lub `float`) - cenę, wyrażoną w złotówkach. Zapamiętaj podaną kwotę jako atrybut `value` i dopilnuj, aby była typu `float` - nawet gdy do `__init__` zostanie przekazana liczba typu `int`. Dodatkowo dopilnuj, aby kwota miała maksymalnie 2 cyfry po przecinku.

Dopisz alternatywne sposoby tworzenia obiektu `Price`, na podstawie kwoty w euro i w dolarach amerykańskich:

```python
some_price = Price.from_usd(25)
some_other_price = Price.from_eur(80)
```

Użyj kursów **EURPLN = 4.5 PLN** oraz **USDPLN = 3.8 PLN**.

Dopisz metodę `__str__`, która przyjmie jeden argument (`self`) i zwróci string - tekst z kwotą, z dopiskiem `PLN` na końcu (ze spacją pomiędzy liczbą a `PLN`).

```python
>>> print(some_price)
95.0 PLN
>>> print(some_other_price)
360.0 PLN
```


# Zadanie 3

Zadanie polega na napisaniu klasy `Student`, która reprezentuje ucznia szkoły podstawowej.

Informacje o uczniu jakie chcemy przechować to:
- imię
- nazwisko
- klasa (np. `'1A'` lub `'5B'`)
- rok urodzenia
- średnia ocen

Takie informacje, w takiej kolejności będą przekazywane w trakcie tworzenia instancji klasy `Student`.

Dodatkowo powinien istnieć sposób na utworzenie wielu instancji klasy `Student` na podstawie listy studentów w pliku `.csv`. Ten sposób powinien pozwalać na opcjonalne przefiltrowanie studentów na podstawie ich klasy - aby otrzymać listę studentów klasy np. `'1A'`.

# Rozwiązanie

Zacznijmy od napisania prostej klasy z metodą `__init__`:

```python
class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg
```

Możemy teraz utworzyć instancje klasy `Student`:

```python
john = Student('John', 'Smith', '1A', 2012, 4.78)
jane = Student('Jane', 'Adams', '2C', 2011, 5.11)
```

Zanim napiszemy metodę wczytującą studentów z pliku, omówimy zagadnienia odczytu plików oraz wydobywania informacji z plików CSV.

## Odczyt plików tekstowych

### Otwieranie

Python posiada funkcję `open(...)`, która zwraca obiekt reprezentujący plik - z tego obiektu, poprzez jego metody możemy otrzymać jego treść na różne sposoby.

Najważniejsze argumenty funkcji `open`:
- `file` - ścieżka do pliku (jeśli plik jest w tym samym folderze co skrypt, wystarczy nazwa pliku),
- `mode` - jaki plik otwieramy i w jakim celu. **Domyślna wartość to `'r'`** i oznacza ona że otwieramy plik tekstowy, w trybie tylko do odczytu. O pozostałych opcjach możesz poczytać [tutaj - funkcja `open` w dokumentacji Pythona](https://docs.python.org/3/library/functions.html#open).

```python
my_file = open('my_file.txt')
```

### Odczyt

Od tej pory w zmiennej `my_file` znajduje się obiekt reprezentujący plik na dysku. Możemy odczytać z niego dane na kilka sposobów:
- `my_file.read()` - zwraca całą zawartość pliku jako string,
- `my_file.readline()` - zwraca tylko jedną linię jako string (plik "pamięta" co zostało już odczytane - kolejne wywołanie metody zwróci kolejną linię),
- `my_file.readlines()` - zwraca wszystkie linie jako listę stringów,

Istnieje jeszcze jeden sposób na odczyt linii z pliku - iteracja po obiekcie:

```python
for line in my_file:
    print('A line from the file:', line)
```

### Zamykanie

Po zakończeniu pracy z plikiem należy go zamknąć:

```python
my_file.close()
```

Istnieje jednak lepszy sposób - można użyć obiektu z plikiem jako tzw. **context manager**. Dzięki temu plik sam się zamknie, gdy skończy się blok kodu który go używa:

```python
with open('my_other_file.txt') as my_other_file:
    print('Is the file closed?', my_other_file.closed)
    data = my_other_file.readline()
    print('Again, is the file closed?', my_other_file.closed)
print('How about now?', my_other_file.closed)  # Notice: no indent like in the lines above
```

Wynikiem będzie:
```
Is the file closed? False
Again, is the file closed? False
How about now? True
```

## Odczyt plików CSV

### Struktura plików

CSV to skrót od Comma Separated Values - i już samo to mówi dużo o tym, jak dane w pliku będą zorganizowane. Pliki CSV służą do przechowywania danych tabelarycznych - linia w pliku to wiersz w tabeli, a poszczególne komórki są w obrębie linii oddzielone przecinkami.

Przykład:

```
1,Fruit of the Loom Girls Socks,7.97,0.60,8.57
2,Rawlings Little League Baseball,2.97,0.22,3.19
3,Secret Antiperspirant,1.29,0.10,1.39
4,Deadpool DVD,14.96,1.12,16.08
5,Maxwell House Coffee 28 oz,7.28,0.55,7.83
6,Banana Boat Sunscreen 8 oz,6.68,0.50,7.18
7,Wrench Set 18 pieces,10.00,0.75,10.75
8,M and M 42 oz,8.98,0.67,9.65
9,Bertoli Alfredo Sauce,2.12,0.16,2.28
10,Large Paperclips 10 boxes,6.19,0.46,6.65
```

### Odczyt

Na szczęście Python w swojej bibliotece standardowej posiada moduł `csv` a w nim funkcję `reader`. Funkcja ta przyjmuje jako argument otwarty plik csv, a zwraca obiekt który pozwala na łatwy odczyt danych z pliku:

```python
import csv

with open('my_file.csv') as my_file:
    my_reader = csv.reader(my_file)
```

Po tak utworzonym obiekcie możemy przeiterować się pętlą `for` - kolejnymi wartościami będą listy stringów, a każdy string będzie odpowiadał kolejnej komórce w wierszu:

```python
import csv

with open('my_file.csv') as my_file:
    my_reader = csv.reader(my_file)
    for row in my_reader:
        print(f'Name: {row[1]}; Price: {row[4]}')
```

Wynikiem będzie:
```
Name: Fruit of the Loom Girls Socks; Price: 8.57
Name: Rawlings Little League Baseball; Price: 3.19
Name: Secret Antiperspirant; Price: 1.39
Name: Deadpool DVD; Price: 16.08
```

## Metoda wczytująca studentów z pliku

Wiemy już jak dane z pliku csv wydobyć, możemy zatem przejść do pisania metody. Nazwiemy ją `from_file`, i na początek będzie wymagała podania tylko nazwy pliku. W obrębie metody utworzymy **wiele** instancji klasy `Student` - przyda się nam zatem lista, w której zapamiętamy te instancje, i którą zwrócimy gdy będzie kompletna.

```python
import csv

class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    @classmethod
    def from_file(cls, file):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                students.append(
                    cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                )
        return students
```

Tak napisana metoda będzie potrafiła odczytać dane z pliku o treści:
```
John,Smith,1A,2012,4.78
Jane,Adams,2C,2011,5.11
Mike,Brown,2C,2011,5.08
```

## Filtrowanie studentów po klasie

Ostatnią funkcjonalnością jakiej wymaga polecenie to filtrowanie studentów po klasie przy odczycie z pliku. Metoda `from_file` otrzyma zatem dodatkowy argument - `class_name`, o domyślnej wartości `None` oznaczającej wyłączenie filtrowania. Nie możemy użyć po prostu `class` jako nazwy argumentu, gdyż jest to słowo kluczowe Pythona.

```python
    ...

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                students.append(
                    cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                )
        return students
```

Metoda przyjmuje już dodatkowy argument, można jej zatem użyć na dwa sposoby:

```python
Student.from_file('students.csv')  # ALL students
Student.from_file('students.csv', '2A')  # Only those in 2A class
```

Zadbajmy o to, aby metoda `from_file` brała pod uwagę podaną nazwę klasy.

W pliku csv nazwa klasy znajduje się w trzeciej kolumnie, czyli pod indeksem 2 (liczymy od zera) w zmiennej `row`. Musimy zadbać o to, aby studenci dopisywali się do listy `students` tylko gdy: `class_name` ma wartość `None` **lub** `class_name` jest takie samo jak `row[2]`:

```python
    ...

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        return students
```

# Podsumowanie

Powyższy przykład ilustruje, że metody z dekoratorem `@classmethod` nie są ograniczone do tworzenia jednej instancji na podstawie innych danych niż oczekuje metoda `__init__`. W tym przpadku metoda zwracała listę wielu instancji, a dane do ich utworzenia nie pochodziły z jej argumentów - wszystkie zostały pobrane z pliku! Python nie narzuca w żaden sposób tego, co metody z dekoratorem `@classmethod` mają zwracać. Python daje nam jedynie narzędzia - to od nas zależy, co z nimi zrobimy.


# Zadanie 4

Napisz klasę `Calculator`, która będzie miała metody:
- `add(a, b)` - zwraca wynik dodawania,
- `sub(a, b)` - zwraca wynik odejmowania,
- `mul(a, b)` - zwraca wynik mnożenia,
- `div(a, b)` - zwraca wynik dzielenia.

Napisz klasę `LoggingCalculator`, która będzie dziedziczyć z klasy `Calculator`.

Klasa `LoggingCalculator` powinna tworzyć atrybut `history` o początkowej wartości pustej listy.

Dopisz do klasy `LoggingCalculator` metody `add`, `sub`, `mul` i `div`, które za pomocą `super()` użyją swoich odpowiedników z klasy `Calculator`, dopiszą string z zapisem wykonanego działania na koniec listy w atrybucie `history`, i dopiero zwrócą wynik.

Przykład:

```python
calc = LoggingCalculator()
print(calc.add(2, 3))
print(calc.mul(3, 3))
print(calc.sub(7, 4))
print(calc.div(5, 2))
print(calc.history)
```

Wynik:

```
5
9
3
['2 + 3 = 5', '3 * 3 = 9', '7 - 4 = 3', '5 / 2 = 2.5']
```

**Do zadania są dołączone testy - możesz je uruchomić poleceniem `python3 -m unittest`.**


# Zadanie 5

Napisz klasę `Book`, której metoda `__init__` przyjmuje trzy argumenty: `title`, `author` oraz `isbn`, i zapamiętuje je w instancji jako atrybuty o tych samych nazwach.

Dopisz metodę `check_isbn`, która przyjmie jeden argument - numer ISBN (jako string), sprawdzi jego poprawność i zwróci `True` lub `False`. Metoda powinna być możliwa do użycia nawet bez instancji klasy `Book` - użyj dekoratora `@staticmethod`.

Do metody `__init__` dopisz kod, który użyje metody `check_isbn`, i rzuci wyjątek `ValueError`, gdy zostanie podjęta próba utworzenia książki (instancji klasy `Book`) z niepoprawnym numerem ISBN.

[Zasady walidacji numerów ISBN](https://pl.wikipedia.org/wiki/Mi%C4%99dzynarodowy_znormalizowany_numer_ksi%C4%85%C5%BCki#Suma_kontrolna) - zaprogramuj sprawdzanie numerów 10 i 13 znakowych, oraz pozwól na podawanie numerów z separatorami (np. `0-306-40615-2`) i bez (np. `0306406152`).
