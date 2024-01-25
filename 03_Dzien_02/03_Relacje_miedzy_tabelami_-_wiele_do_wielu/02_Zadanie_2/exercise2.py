create_screenings_table = """
CREATE TABLE screening(
    id SERIAL PRIMARY KEY, 
    datetime TIMESTAMP, 
    cinema_id INT, 
    movie_id INT, 
    FOREIGN KEY(cinema_id) REFERENCES cinemas(id), 
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
"""

add_screenieng_1 = """
INSERT INTO screening(cinema_id, movie_id, datetime) VALUES (1, 2, '2024-02-12 12:35:00');
"""

add_screenieng_2 = """
INSERT INTO screening(cinema_id, movie_id, datetime) VALUES (3, 2, '2021-12-12 23:12:22');
"""

add_screenieng_3 = "Write the query here!"
