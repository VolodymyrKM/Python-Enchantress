set_table = """DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE users
       (
        id SERIAL PRIMARY KEY,
        name VARCHAR (50) UNIQUE NOT NULL,
        email VARCHAR (255),
        registration_time TIMESTAMP
       );


CREATE TABLE cart
       (
        id SERIAL PRIMARY KEY,
        creation_time TIMESTAMP,
        user_id INT, CONSTRAINT fk_user  FOREIGN KEY(user_id) REFERENCES users(id)
       );

CREATE TABLE cart_details
(
        id SERIAL PRIMARY KEY,
        cart_id INT,
        price INT,
        product VARCHAR(255),
        CONSTRAINT fk_cart_id FOREIGN KEY(cart_id) REFERENCES cart(id)

);"""