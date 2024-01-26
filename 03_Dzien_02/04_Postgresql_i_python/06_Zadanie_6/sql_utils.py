from flask import Flask
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


@app.route('/movie/delete/<int:movie_id>/')
def delete_movie(movie_id):

    # sprawdzenie, czy film o podanym id istnieje
    query = f"SELECT name from movies WHERE id={movie_id}"
    result = execute_sql(query, 'cinemas_db')

    # jeżeli istnieje to usuwamy
    if result:
        query = f"DELETE FROM movies WHERE id={movie_id};"
        execute_sql(query, 'cinemas_db')

        return f"Film '{result[0][0]}' został usunięty"
    # w przeciwnym razie wyświetlamy informacje o braku takiego filmu
    else:
        return "Film o podanym id nie istnieje"


if __name__ == "__main__":
    app.run(debug=True)
