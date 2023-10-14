import psycopg2
import visualizator
import db

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234567890", port=5432)

cur = conn.cursor()

db.clear_tables(cur)

cur.execute("""CREATE TABLE IF NOT EXISTS worker (
id serial PRIMARY KEY,
name VARCHAR(255),
password VARCHAR(255))""")

cur.execute("""CREATE TABLE IF NOT EXISTS meeting_rooms (
id SERIAL PRIMARY KEY,
meeting_roomsId INTEGER REFERENCES worker(id),
description VARCHAR(255),
date DATE,
time TIME)""")

cur.execute("""INSERT INTO worker (name, password) VALUES ('bob', '1234')""")

visualizator.visualize_tables(cur)

conn.commit()

cur.close()
conn.close()
