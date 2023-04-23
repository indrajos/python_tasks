-- Create a database.

CREATE DATABASE webstore;

-- Create tables based on the ERD what You developed in the Assignment No.1

CREATE TABLE IF NOT EXISTS webstore.supplier (
  supplier_id 		integer AUTO_INCREMENT PRIMARY KEY,
  supplier_name 	varchar(50) NOT NULL,
  phone 			bigint NOT NULL,
  email 			text NOT NULL 
);

CREATE TABLE IF NOT EXISTS webstore.customer (
  customer_id 		integer AUTO_INCREMENT PRIMARY KEY,
  customer_name 	varchar(50) NOT NULL,
  customer_surname 	varchar(50) NOT NULL,
  phone 			bigint NOT NULL,
  email 			text NOT NULL 
);

CREATE TABLE IF NOT EXISTS webstore.product (
  product_id 		integer AUTO_INCREMENT PRIMARY KEY,
  title 			varchar(50) NOT NULL,
  description 		text,
  price 			float NOT NULL,
  warranty_months 	integer,
  category_name 	text NOT NULL,
  supplier_id 		integer NOT NULL REFERENCES supplier(supplier_id)
);
-- categories: portable computers, PCs, software, accessories

CREATE TABLE IF NOT EXISTS webstore.orders (
  order_id 			integer AUTO_INCREMENT PRIMARY KEY,
  order_date 		date NOT NULL,
  customer_id 		integer NOT NULL REFERENCES customer(customer_id),
  product_id 		integer NOT NULL REFERENCES product(product_id),
  product_amount 	integer NOT NULL,
  status 			text NOT NULL 
);
-- statuses for the order - entered = > in 
-- processing = > (canceled) = > delivered and paid (done). 


-- Add 3 records at each table.
INSERT INTO webstore.supplier
VALUES (1, 'ACME', 37065454541, 'info@acme.com'),
		(2, 'Lenovo', 37069922333, 'info@lenovo.lt'),
		(3, 'Apple', 37061877889, 'info@apple.lt');

INSERT INTO webstore.customer
VALUES (1, 'John', 'Snow', 37065454545, 'john@yahoo.com'),
		(2, 'Kristi', 'Smith', 37064545454, 'kristi@something.com'),
		(3, 'Peter', 'Rain', 37061234567, 'peter@email.com');
	
INSERT INTO webstore.product
VALUES (1, 'Laptop', 'very good laptop', 1200, 24, 'portable computers', 2),
		(2, 'usb memory stick', 'very small', 3, 6, 'accessories', 1),
		(3, 'computer', 'super fast', 1893, 24, 'PCs', 3);
	
INSERT INTO webstore.orders
VALUES (1, '2023-01-08', 1, 2, 2, 'delivered'),
		 (2, '2023-02-08', 2, 1, 1, 'processing'),
		 (3, '2023-02-08', 2, 2, 1, 'processing'),
		 (4, '2023-01-09', 3, 3, 1, 'delivered');


-- Try to update some records.
UPDATE webstore.orders  
SET status = 'delivered'
WHERE customer_id = 2 AND order_date = '2023-02-08';

-- Try to delete one record.
DELETE FROM webstore.product WHERE product_id = 3;

-- Try to build 3 simple SELECT statements with WHERE, ORDER BY.
SELECT * FROM webstore.orders o 
WHERE customer_id = 2
ORDER BY product_amount;

SELECT * FROM webstore.product p 
WHERE warranty_months = 24
ORDER BY price DESC;

SELECT customer_surname FROM webstore.customer
WHERE customer_name LIKE 'K%';

-- Try to build 3 advanced SELECT statements with JOIN.
SELECT s.supplier_name, p.title, p.price 
FROM webstore.supplier s
INNER JOIN webstore.product p  
ON s.supplier_id = p.supplier_id;

SELECT o.status, c.email 
FROM webstore.orders o 
LEFT JOIN webstore.customer c 
ON o.customer_id = c.customer_id;

SELECT o.order_date, p.category_name 
FROM webstore.orders o 
INNER JOIN webstore.product p 
ON o.product_id = p.product_id ;
