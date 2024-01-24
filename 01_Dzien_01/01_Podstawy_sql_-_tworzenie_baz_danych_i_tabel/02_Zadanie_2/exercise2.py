sql1 = """
CREATE TABLE products (
     id SERIAL,
     name VARCHAR(256),
     description TEXT,
     price DECIMAL(5,2)
);
"""

sql2 = """
CREATE TABLE orders (id SERIAL, description TEXT);
"""

sql3 = """
CREATE TABLE clients (id SERIAL, name VARCHAR(256), surname VARCHAR(256));
"""
