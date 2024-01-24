![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; zadania rozwiązywane z wykładowcą

Napisz funkcję `execute_sql` uruchamiającą dowolny kod sql. Funkcja powinna przyjąć dwa parametry:
* nazwę bazy danych.
* zapytanie SQL.

Funkcja powinna wykonać podany w parametrze kod sql na podanej bazie.
Funkcja powinna zwrócić listę wyników (w przypadku zapytań typu **SELECT**), lub `None`.

Rozwiązanie umieść w pliku **sql_utils.py**.


## Zadanie 2 &ndash; zadania rozwiązywane z wykładowcą

Używając Flaska, napisz program, który wyświetli na stronie wszystkie produkty znajdujące się w bazie danych o nazwie
 `exercises_db`.

**Podpowiedź:** Program powinien uruchamiać zapytanie SQL, które wyciągnie wszystkie wpisy z odpowiedniej tabeli,
po czym wyświetli je na ekranie. Możesz wykorzystać kod napisany w poprzednim zadaniu.

Rozwiązanie umieść w pliku **sql_utils.py**.


## Zadanie 3

1. W pliku **form.html** jest formularz służący do tworzenia nowych wpisów w tablicach.
Przeanalizuj HTML i użyj tego kodu w dalszej części zadania.
2. Używając Flaska napisz program, który:
  * po wejściu metodą **GET** wyświetli formularz zawierający następujące pola:
    * `name` - nazwa filmu,
    * `description` - opis filmu,
    * `rating` - ocena filmu,
  * po wejściu metodą **POST** sprawdzi, czy formularz został wypełniony poprawnie:
    * jeśli tak, to zapisze film do bazy danych,
    * jeśli nie, zwróci odpowiedni komunikat.

Program udostępnij pod adresem `add_movie`.  
Możesz wykorzystać fukcje utworzone w poprzednich zadaniach.


## Zadanie 4

Używając Flaska, napisz stronę, która:
* będzie dostępna pod adresem `movies`,
* pobierze z bazy danych wszystkie filmy
* wyświetli je na stronie w formie listy.    


## Zadanie 5 (*)

Używając Flaska, napisz stronę, która:
* będzie dostępna pod adresem `movie/<movie_id>`, gdzie `movie_id`, to liczba określająca **id** filmu,
* pobierze z bazy informacje na temat filmu o podanym ID,
* wyświetli je na stronie.    


## Zadanie 6 (*)

Używając Flaska, napisz stronę, która usunie wybrany film o podanym **id**. Id powinno być przekazane w adresie strony.
Strona powinna wyświetać informacje o usunięciu wpisu z tabeli.


## Zadanie 7 (*)

Używając Flaska, napisz stronę, do której przekażesz id filmu metodą GET. Strona powinna:

- wyciągnąć dane filmu z bazy danych; w razie podania błędnego identyfikatora filmu,
powinna wyświetlić komunikat „nie ma takiego filmu.”
- wyświetlić formularz, w którym będą następujące pola:
  - id filmu (pole ukryte, niemożliwe do edycji),
  - tytuł filmu,
  - opis filmu.

Każde z tych pól, pownno być wypełnione danymi wyciągnietymi z bazy danych.

Po wysłaniu formularza (metodą POST), program powinien:

- wyciagnąć dane filmu z bazy danych,
- wygenerować odpowiednie zapytanie, które **zmieni** dane filmu w bazie,
- wykonać to zapytanie,
- gdy wszystko zakończy się poprawnie, wyświetlić komunikat „zmieniono dane filmu”,
- w przypadku błędu, wyświetlić komunikat „ups... coś poszło źle!”.


Najpierw przetestuj zapytania SQL w konsoli lub panelu administracyjnym,
dopiero potem napisz kod Pythona.

**Uwaga: Jeśli w poleceniu widnieje „napisz stronę”, oznacza to, że należy
napisać program w Pythonie, używając Flaska, który będzie się komunikował z
użytkownikiem za pomocą stron WWW i protokołu HTTP.**
