"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1616')


try:
    with conn:
        with conn.cursor() as cur:

            with open('north_data\\customers_data.csv', 'r') as csvfile:
                header = next(csvfile)
                csvreader = csv.reader(csvfile)
                query = "INSERT INTO customers VALUES (%s, %s, %s);"
                for row in csvreader:
                    cur.execute(query, row)

            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            for row in rows:
                print(row)

            with open('north_data\\employees_data.csv', 'r') as csvfile:
                header = next(csvfile)
                csvreader = csv.reader(csvfile)
                query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s);"
                for row in csvreader:
                    cur.execute(query, row)

            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)

            with open('north_data\\orders_data.csv', 'r') as csvfile:
                header = next(csvfile)
                csvreader = csv.reader(csvfile)
                query = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s);"
                for row in csvreader:
                    cur.execute(query, row)

            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
    conn.close()
