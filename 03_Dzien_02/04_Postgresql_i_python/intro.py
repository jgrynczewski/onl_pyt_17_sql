from psycopg2 import connect, ProgrammingError

# query = "DELETE FROM opinions where id=2;"
# query = "SELECT * FROM opinions;"
query = "SELECT * FROM products;"

# połączenie z bazą
cnx = connect(
    user="postgres",
    password="postgres",
    database='exercises_db'
)

# tworzymy kursor
with cnx.cursor() as cursor:
    # zapytanie
    cursor.execute(query)
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


# Konsumowanie
if res:
    for item in res:
        print(item[1])
