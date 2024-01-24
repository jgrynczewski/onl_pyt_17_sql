![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; zadania rozwiązywane z wykładowcą

Stwórz nową bazę danych o nazwie `exercises_db`. Polecenie zapisz do zmiennej w pliku **zadanie1.py**


## Zadanie 2 &ndash; zadania rozwiązywane z wykładowcą

W bazie danych o nazwie ```exercises_db``` stwórz następujące tabele:

* Products:
  * id: serial
  * name: string
  * description: string
  * price: float(5,2)
* Orders:
  * id: serial
  * description: string
* Clients:
  * id: serial
  * name: string
  * surname: string


Polecenie zapisz do zmiennej w pliku **zadanie2.py**


## Zadanie 3

Stwórz nową bazę danych o nazwie ```cinemas_db```. Kod SQL zapisz do zmiennej w pliku **zadanie3.py**.


## Zadanie 4

W bazie danych o nazwie ```cinemas_db``` stwórz następujące tabele (pamietaj o tym, że wszystkie nazwy powinny
być zapisane w języku angielskim):

* Cinemas:
  * id: serial
  * name: string
  * address: string
* Movies:
  * id: serial
  * name: string
  * description: string
  * rating: int
* Tickets:
  * id: serial
  * quantity: int
  * price: float
* Payments:
  * id: serial
  * type: string
  * date: date

1. Załóż odpowiednie atrybuty na pola (np. każde **id** powinno być kluczem głównym, być automatycznie numerowane).
2. Napisz odpowiednie zapytania SQL.
3. Polecenie SQL zapisz do zmiennej w pliku **zadanie4.py**.
4. Pamiętaj, że jeśli baza o podanej nazwie już istnieje, nie da się jej utworzyć ponownie. Najpierw trzeba ją usunąć.
4. Dokładnie czytaj kody błędów zwracane przez bazę danych.

**Podpowiedź:** Dla typu string użyj pola typu varchar lub text, w zależności od potrzeb.
