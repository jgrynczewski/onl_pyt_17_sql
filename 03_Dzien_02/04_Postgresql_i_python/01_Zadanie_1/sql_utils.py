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
    # Place exercise 1 solution here.

    # połączenie z bazą
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


result = execute_sql(
    sql_code="SELECT * FROM opinions;",
    # sql_code="INSERT INTO opinions(description, product_id) VALUES ('Taki sobie', 2);",
    db='exercises_db'
)

print(result)
