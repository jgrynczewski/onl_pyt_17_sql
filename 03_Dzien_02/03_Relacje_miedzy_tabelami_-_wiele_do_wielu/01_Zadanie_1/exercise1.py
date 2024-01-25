create_products_orders = """
CREATE TABLE products_orders(
    id SERIAL PRIMARY KEY, 
    products_id INT, 
    orders_id INT, 
    FOREIGN KEY(products_id) REFERENCES products(id), 
    FOREIGN KEY(orders_id) REFERENCES orders(id)
);
"""

add_product_order_1 = """
INSERT INTO products_orders(products_id, orders_id) VALUES (2,1);
"""

add_product_order_2 = """
INSERT INTO products_orders(products_id, orders_id) VALUES (2,3);
"""

add_product_order_3 = """
INSERT INTO products_orders(products_id, orders_id) VALUES (3,2);
"""

add_product_order_4 = """
INSERT INTO products_orders(products_id, orders_id) VALUES (3,3);
"""
