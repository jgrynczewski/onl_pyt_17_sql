create_table_client_address = """
CREATE TABLE client_address(
    id SERIAL, 
    city VARCHAR(100), 
    street VARCHAR(100), 
    house_nr VARCHAR(32), 
    client_id INT, PRIMARY KEY(id), 
    FOREIGN KEY(client_id) REFERENCES clients(id)
);
"""

add_client_address_1 = """
INSERT INTO client_address(city, street, house_nr, client_id) VALUES ('Warsaw', 'Kwacza', 20, 5);
"""

add_client_address_2 = """
INSERT INTO client_address(city, street, house_nr, client_id) VALUES ('Cracow', 'Myszy', 40, 6);
"""

add_client_address_3 = """
INSERT INTO client_address(city, street, house_nr, client_id) VALUES ('Unknown', 'Anonymous', 0, 8);
"""
