sql = """
CREATE TABLE cinemas (id SERIAL PRIMARY KEY, name VARCHAR(256), address VARCHAR(256));
"""

sql2 = """
CREATE TABLE movies (id SERIAL PRIMARY KEY, name VARCHAR(256), description VARCHAR(256), rating INTEGER);
"""

sql3 = """
CREATE TABLE tickets (id SERIAL PRIMARY KEY, quantity INTEGER, price DECIMAL);
"""

sql4 = """
CREATE TABLE payments (id SERIAL PRIMARY KEY, type VARCHAR(256), date DATE);
"""
