![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python i bazy danych &ndash; praca domowa &ndash; Dzień 2

Połącz tabele relacjami:
1. autorów i książki (relacja jeden do wielu); dla uproszczenia przyjmij, że książka może mieć tylko jednego autora;
wystarczy, że przeedytujesz odpowiednie tabele,
2. książki i kategorie (relacja wiele do wielu); jedna ksiązka może mieć wiele kategorii, jedna kategoria może należeć
do wielu ksiązek; dodaj odpowiednią tabelę pośrednią,
3. klientów i książki (relacja wiele do wielu); W tabeli pośredniej, dodaj pola:
    * loan_date: date (data wypożyczenia)
    * return_date: date (data zwrotu, domyślnie Null)


Używając **Flaska** Napisz aplikację, do zarządzania naszą biblioteką. W aplikacji powinny być następujące strony:
1. `books` - lista wszystkich książek,
2. `add_book` - strona, która:
    * po wejściu metodą **GET** wyświetli formularz dodania książki, 
    * po wejściu metodą **POST** doda książkę do bazy danych,
3. `book_details/<id>` - strona wyświetlająca szczegółowe dane książki,       
4. `delete_book/<id>` - strona umożliwiająca usunięcie książki o podanym id  
5. `clients` - lista wszystkich klientów,
6. `add_client` - strona, która:
    * po wejściu metodą **GET** wyświetli formularz dodania klienta, 
    * po wejściu metodą **POST** doda klienta do bazy danych,  
7. `delete_client/<id>` - strona umożliwiająca usunięcie klienta o podanym id
8. `client_details/<id>` - strona wyświetlająca szczegółowe dane klienta, 
w tym wszystkie wypożyczone przez niego ksiązki
9. loan - strona umożliwiająca wypożyczenie książki:
  * po wejściu metodą **GET** powinna wyświetlić formularz z listą klientów i ksiązek
  * po wejściu metodą **POST** powinna dodać wypożyczenie do bazy danych      


(*) Aplikacje możesz rozwinąć według własnego uznania dodając inne przydatne funkcjonalności. np.:
    * zarządzanie kategoriami,
    * stronę zwrotu książki,
    * blokadę wypożyczeń (mechanizm pozwalający wypożyczyc tylko jedną książkę przez jednego klienta w danym czasie)
    * możliwość oceniania książek,
    * możliwość komentowania książek.
    
----

### Zadanie: poćwicz SQL (*)

W repozytorium z zadaniami domowymi znajdziesz zrzut bazy danych **football.sql**. 
Jest to baza danych z wynikami Ligi Okręgowej Warszawa II w sezonie 2016/17 (wyniki na dzień 14 listopada 2016 roku).

Utwórz na serwerze bazę danych i zaimportuj plik SQL. Jeśli nie wiesz, jak to zrobić, poszukaj w Google,
używając słów kluczowych: *PostgreSQL, import, dump*.

Przyjrzyj się strukturze i danym. Znajdują się tam dwie tabele: **Teams** i **Games**. 
Pierwsza z nich to lista klubów piłkarskich i punkty zdobyte do dnia eksportu bazy danych. 
Druga tabela to wyniki gier. Pola `team_home` i `team_away` to klucze obce do tabeli **Teams**

Napisz zapytania, które:

1. Wyciągną klub, który jest liderem tabeli,
2. Wyciągną tabelę, posortowaną według liczby zdobytych punktów,
3. Wyciągną wszystkie mecze, które Naprzód Brwinów grał u siebie,
4. Wyciągną wszystkie mecze, które Naprzód Brwinów grał na wyjeździe,
5. Wyciągną wszystkie mecze (u siebie i na wyjeździe) klubu Naprzód Brwinów. 
6. Zsumują wszystkie gole zdobyte przez klub Naprzód Brwinów u siebie i na wyjeździe 
(zrób dwa zapytania: osobno u siebie, osobno na wyjeździe).

W podpunktach 3 - 5 wynik ma zawierać kolejno: 

* nazwę klubu gospodarzy,
* nazwę klubu gości,
* liczbę goli strzelonych przez gospodarzy,
* liczbę goli strzelonych przez gości.  
