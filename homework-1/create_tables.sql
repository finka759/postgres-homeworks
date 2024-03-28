CREATE DATABASE north WITH OWNER = postgres ENCODING = 'UTF8' LOCALE_PROVIDER = 'libc' CONNECTION LIMIT = -1 IS_TEMPLATE = False;
-- SQL-команды для создания таблиц --
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	employee_email VARCHAR(255) UNIQUE NOT NULL,
	employee_firstname VARCHAR(255) NOT NULL,
	employee_lastname VARCHAR(255)
);

CREATE TABLE customers
(
	customer_id int PRIMARY KEY,
	customer_email VARCHAR(255) UNIQUE NOT NULL,
	customer_firstname VARCHAR(255) NOT NULL,
	customer_lastname VARCHAR(255)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	order_datatime timestamp NOT NULL,
	order_pay money,
	customers_customer_id int REFERENCES customers(customer_id) NOT NULL,
	employees_employee_id int REFERENCES employees(employee_id) NOT NULL
);

