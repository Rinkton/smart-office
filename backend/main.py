import visualizator
import db

cur, conn = db.connect()

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

cur.execute("""INSERT INTO worker (name) VALUES ('BOB')""")
cur.execute("""INSERT INTO meeting_rooms (meeting_roomsId, description, date, time) VALUES (1, '1234', '1998-01-07', '10:10:10')""")

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

id = 1
cur.execute("""INSERT INTO worker (name) VALUES ('BOB')""")
cur.execute("""INSERT INTO meeting_rooms (meeting_roomsId, description, date, time) VALUES (1, '1234', '1998-01-07', '10:10:10')""")
cur.execute(
        f"""SELECT id meeting_roomsId, description, date, time FROM meeting_rooms WHERE id=1""")
print(cur.fetchall())

visualizator.visualize_tables(cur)

db.disconnect(cur, conn)
