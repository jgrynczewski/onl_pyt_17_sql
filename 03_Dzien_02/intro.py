# 1 do 1
""""""
"""
CREATE  TABLE capital(
    id SERIAL,
    name VARCHAR(100),
    PRIMARY KEY(id)
);

CREATE TABLE country(
    id SERIAL,
    name VARCHAR(100),
    capital_id INT UNIQUE,
    PRIMARY KEY(id),
    FOREIGN KEY(capital_id) REFERENCES capital(id)
);
"""

# 1 do wielu
"""
CREATE TABLE city(
    id SERIAL, 
    name VARCHAR(200), 
    country_id INT, 
    PRIMARY KEY(id), 
    FOREIGN KEY(country_id) REFERENCES country(id)
);
"""

# wiele do wielu
