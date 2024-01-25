create_opinions_table = """
CREATE TABLE opinions(
    id SERIAL PRIMARY KEY, 
    description TEXT, 
    product_id INT, 
    FOREIGN KEY(product_id) REFERENCES products(id)
);
"""

add_opinions = """
INSERT INTO opinions(description, product_id) VALUES 
    ('Super!!', 2), 
    ('Tak sobie', 2), 
    ('Szybki!', 3);
"""

select_opinions = """
select * from opinions where product_id=2;
"""
