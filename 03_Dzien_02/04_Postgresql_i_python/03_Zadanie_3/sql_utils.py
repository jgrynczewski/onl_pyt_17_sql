from flask import Flask, render_template, request
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
    # Place exercise 2 solution here.
    cnx = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=db
    )

    # tworzymy kursor
    with cnx.cursor() as cursor:
        # zapytanie
        cursor.execute(sql_code)
        # commit
        cnx.commit()

        try:
            # fetchujemy (dla SELECT)
            res = cursor.fetchall()
        except ProgrammingError:
            # jeżeli nic nie było do sfechowania (bo zapytanie INSERT, UPDATE lub DELETE)
            res = None

    # Zamykamy połączenie z bazą
    cnx.close()

    return res


app = Flask(__name__)


@app.route('/add_movie/', methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        return render_template('form.html')

    elif request.method == "POST":
        data = request.form
        name = data.get('name')
        desc = data.get('desc')
        rating = data.get('rating')

        if name and desc and rating:
            query = f"INSERT INTO movies(name, description, rating) VALUES ('{name}', '{desc}', {rating})"
            execute_sql(query, 'cinemas_db')
            return "Pomyślnie dodano nowy film"
        else:
            return "Wprowadzono niepoprawne dane"


if __name__ == "__main__":
    app.run(debug=True)

