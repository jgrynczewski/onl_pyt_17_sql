from flask import Flask
from psycopg2 import connect, ProgrammingError

USER = "postgres"
HOST = "localhost"
PASSWORD = "postgres"


def create_db(db):
    """
    Create db with given name.

    :param str db: name of db
    """
    # Place exercise 1 solution here.
    pass


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


@app.route('/products/')
def hello():
    products = execute_sql("SELECT * FROM products", "exercises_db")

    # budujemy odpowiedź
    response = "<h3>Lista produktów</h3><ul>"
    for product in products:
        response += f"<li>{product[1]} [{product[2]}]</li>"
    response += "</ul>"

    return response


if __name__ == "__main__":
    app.run(debug=True)

