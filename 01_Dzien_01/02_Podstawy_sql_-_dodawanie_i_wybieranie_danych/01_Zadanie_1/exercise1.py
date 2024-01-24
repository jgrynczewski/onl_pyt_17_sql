add_products_sql = """
INSERT INTO products(name, description, price) VALUES
    ('lizak', 'truskawkowy', 10),
    ('bmv', 'czarne', 999),
    ('rower', 'bmx', 100)
;
"""

add_orders_sql = """
INSERT INTO orders(description) VALUES ('pierwsze'), ('drugie'), ('trzecie');
"""

add_clients_sql = """
INSERT INTO clients(name, surname) VALUES ('Donald', 'Duck');
INSERT INTO clients(name, surname) VALUES ('Micky', 'Mouse');
INSERT INTO clients(name, surname) VALUES ('Sknerus', 'McKwacz');
INSERT INTO clients(name, surname) VALUES
    ('John', 'Doe'),
    ('Jane', 'Doe')
;
"""
