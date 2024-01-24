add_movies = """
INSERT INTO movies (name) VALUES ('Wall Street'), ('Witness'), ('Startreck'), ('Deep Space Nine');
"""
add_tickets = """
INSERT INTO tickets (quantity, price) VALUES (1, 10), (2, 30), (4, 15), (5, 25);
"""

get_movies = """
SELECT name FROM movies WHERE 'W%';
"""

get_tickets_1 = """
SELECT * FROM tickets WHERE price>15.30;
"""

get_tickets_2 = """
SELECT * FROM tickets WHERE quantity>3;
"""
