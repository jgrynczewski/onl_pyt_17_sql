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


@app.route('/movie/<int:movie_id>/')
def hello(movie_id):
    query = f"SELECT * FROM movies WHERE id={movie_id};"

    movie = execute_sql(query, "cinemas_db")

    if movie:
        movie = movie[0]
        response = f"""
        <p>Nazwa: {movie[1]}</p>
        <p>Opis: {movie[2]}</p>
        <p>Ocena: {movie[3]}</p>
        """

    return response


if __name__ == "__main__":
    app.run(debug=True)
