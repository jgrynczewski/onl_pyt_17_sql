![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; zadania rozwiązywane z wykładowcą

Stwórz nową tabelę `ClientAddress` zawierającą:

* city: string
* street: string
* house_nr: string

Tabela `ClientAddress` ma być połączona relacją jeden do jednego z tabelą
`Clients`. Napisz kilka zapytań SQL, które wprowadzą adresy dla istniejących
już użytkowników.

Zapytania umieść w pliku **zadanie1.py**.

---

## Zadanie 2

Stwórz tabelę płatności. Ma mieć takie same dane jak w zadaniach z
poprzedniego dnia, ale z tabelą `Ticket` ma być powiązana relacją jeden do
jednego (wpłynie to na kolumnę **id**). Relacja między biletem a płatnością
jest następująca: bilet ma 1 lub 0 płatności (jest wtedy nieopłacony) &ndash;
płatność musi być przypisana do biletu.

Zapytania umieść w pliku **zadanie2.py**.
