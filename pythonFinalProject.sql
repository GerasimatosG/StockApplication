CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price FLOAT ,
    availability INT 
);

INSERT INTO items (name, description, price, availability) VALUES
('Laptop', 'A high-performance laptop suitable for all your needs.', 999.99, 10),
('Smartphone', 'A latest model smartphone with all the newest features.', 699.99, 25),
('Headphones', 'Noise-cancelling over-ear headphones.', 199.99, 50),
('Smartwatch', 'A smartwatch with various health-tracking features.', 249.99, 15),
('Tablet', 'A lightweight tablet perfect for media consumption.', 329.99, 20);