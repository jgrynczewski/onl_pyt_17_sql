![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python i bazy danych – praca domowa – Dzień 1

Twoim zadaniem będzie stworzenie oprogramowania do zarządzania biblioteką. Pamiętaj, żeby wszystkie zapytania zapisywać
w pliku. Przydadzą się nam w późniejszej pracy. Wykonaj następujące zadania:

1. Przygotuj bazę danych o nazwie **library_db**
2. Stwórz tabele:
    * Author:
      * id: serial
      * name: string
    * Book:
      * id: serial
      * ISBN: string (max 13 znaków)
      * name: string
      * description: string
      * is_loaned: bool, (domyślnie False)
    * Client:
      * id: serial
      * first_name: string
      * last_name: string
    * Category:
      * id: serial
      * name: string
3. Dodaj do bazy danych:
    * 5 autorów,
    * 10 ksiązek,
    * 3 klientów.
4. Napisz zapytania, wyciągające dane z bazy:
    * listę wszystkich autorów,
    * autora o id `2`,
    * listę wszystkich książek,
    * książkę o id `2`,
    * listę wszystkich klientów,
    * klienta o id `1`.
5. Napisz zapytanie, którym usuniesz książkę o id równym `5`.  
