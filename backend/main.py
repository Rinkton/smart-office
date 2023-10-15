import visualizator
import db

cur, conn = db.connect()

db.clear_tables(cur, conn)

db.create_tables(cur)

cur.execute("""INSERT INTO users (name, role, password) VALUES ('Владислав', 'worker', '1234')""")

visualizator.visualize_tables(cur)

db.disconnect(cur, conn)
