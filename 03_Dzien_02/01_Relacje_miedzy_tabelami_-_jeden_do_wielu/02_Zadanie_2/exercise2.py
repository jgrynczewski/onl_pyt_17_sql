create_comments_table = """
CREATE TABLE comments (
    id SERIAL PRIMARY KEY, 
    content TEXT, 
    movie_id INT, 
    FOREIGN KEY(movie_id) REFERENCES movies(id));
"""

add_comments = """
INSERT INTO comments (content, movie_id) VALUES 
    ('super', 3), 
    ('fajne', 3), 
    ('ok', 2);
"""
