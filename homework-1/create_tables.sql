CREATE DATABASE north WITH OWNER = postgres ENCODING = 'UTF8' LOCALE_PROVIDER = 'libc' CONNECTION LIMIT = -1 IS_TEMPLATE = False;
-- SQL-команды для создания таблиц --
CREATE TABLE customers
(
	customer_id VARCHAR(255) PRIMARY KEY,
	company_name VARCHAR(255),
	contact_name VARCHAR(255)
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	firstname VARCHAR(255) NOT NULL,
	lastname VARCHAR(255),
	title VARCHAR(255),
	birth_date VARCHAR(25),
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id VARCHAR(255) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date  VARCHAR(25) NOT NULL,
	ship_city VARCHAR(255)
);
