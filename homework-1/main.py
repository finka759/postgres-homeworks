"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from datetime import datetime, timezone

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1616')

try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employees VALUES (%s,%s, %s,%s)", (1, 'e_el_1', 'e_fn_1', 'e_ln_1'))
            cur.execute("INSERT INTO employees VALUES (%s,%s, %s,%s)", (2, 'e_el_2', 'e_fn_2', 'e_ln_2'))
            cur.execute("INSERT INTO employees VALUES (%s,%s, %s,%s)", (3, 'e_el_3', 'e_fn_3', 'e_ln_3'))
            cur.execute("INSERT INTO employees VALUES (%s,%s, %s,%s)", (4, 'e_el_4', 'e_fn_4', 'e_ln_4'))

            cur.execute("SELECT * FROM employees")

            cur.execute("INSERT INTO customers VALUES (%s,%s, %s,%s)", (1, 'c_el_1', 'c_fn_1', 'c_ln_1'))
            cur.execute("INSERT INTO customers VALUES (%s,%s, %s,%s)", (2, 'c_el_2', 'c_fn_2', 'c_ln_2'))
            cur.execute("INSERT INTO customers VALUES (%s,%s, %s,%s)", (3, 'c_el_3', 'c_fn_3', 'c_ln_3'))
            cur.execute("INSERT INTO customers VALUES (%s,%s, %s,%s)", (4, 'c_el_4', 'c_fn_4', 'c_ln_4'))

            cur.execute("SELECT * FROM customers")
            dt = datetime.now(timezone.utc)
            cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", (1, dt, 10, 1, 2))
            cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", (2, dt, 11, 2, 4))
            cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", (3, dt, 12, 3, 3))
            cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", (4, dt, 13, 4, 1))

            cur.execute("SELECT * FROM orders")

            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
    conn.close()
