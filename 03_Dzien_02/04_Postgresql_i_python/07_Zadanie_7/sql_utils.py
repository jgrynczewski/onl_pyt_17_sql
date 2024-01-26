from flask import Flask, request
from psycopg2 import connect, ProgrammingError

USER = "postgres"
HOST = "localhost"
PASSWORD = "postgres"


def execute_sql(sql_code, db):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    cnx = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=db
    )

    with cnx.cursor() as cursor:
        cursor.execute(sql_code)
        cnx.commit()

        try:
            res = cursor.fetchall()
        except ProgrammingError:
            res = None

    cnx.close()
    return res


app = Flask(__name__)


@app.route('/movie/update/<int:movie_id>/', methods=["GET", "POST"])
def delete_movie(movie_id):
    # sprawdzenie, czy film o podanym id istnieje (niezależnie od tego czy zapytanie przyszło metodą get czy post)
    query = f"SELECT * from movies WHERE id={movie_id};"
    result = execute_sql(query, 'cinemas_db')

    # jeżeli nie istnieje zwracamy stosowny komunikat
    if not result:
        return f"Film o id {movie_id} nie istnieje"

    # w przeciwnym razie
    else:
        # jeżeli zapytanie przesłane metodą get, to wsadzamy wyciągnięte z bazy informacje do formularza
        if request.method == "GET":
            result = result[0]
            # tworzymy formularz (dane wyciągnięte z bazy wsadzamy w odpowiednie miejsca)
            # input typu hidden z name=id tworzymy tylko dlatego, że tak podano w treści zadania (do niczego nie jest
            # potrzebne)
            response = f"""
                <form method="POST">
                    <input type=hidden name=id value={result[0]}>
                    <input type=text name=title value="{result[1]}">
                    <input type=text name=description value="{result[2]}">
                    <input type=submit value=Zmodyfikuj>
                </form>
            """
            return response

        # jeżeli zapytanie przesłane metodą post to wyciągamy dane formularza (request.form), sprawdzamy czy wszystkie
        # są i jeżeli tak to tworzymy z nich zapytanie UPDATE do bazy danych
        elif request.method == "POST":
            # wyciągamy dane z formularza
            data = request.form
            title = data.get('title')
            description = data.get('description')

            # jeżeli w danych formularza były wszystkie potrzebne informacje to tworzymy zapytanie UPDATE
            if title and description:
                query = f"UPDATE movies SET name='{title}', description='{description}' WHERE id={movie_id};"
                result = execute_sql(query, 'cinemas_db')
                return "Zaktualizowano informacje o filmie"
            # w przeciwnym razie wysyłamy stosowny komunikat
            else:
                return "Podano niepoprawne dane"


if __name__ == "__main__":
    app.run(debug=True)
