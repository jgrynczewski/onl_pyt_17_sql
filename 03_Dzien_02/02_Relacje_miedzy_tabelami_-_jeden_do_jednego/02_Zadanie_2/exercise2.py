create_table_payments = """
CREATE TABLE payments(
    id SERIAL PRIMARY KEY, 
    type VARCHAR(256), 
    date DATE,
    ticket_id INT, 
    FOREIGN KEY(ticket_id) REFERENCES tickets(id)
);
"""