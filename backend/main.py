import visualizator
import db

cur, conn = db.connect()

db.clear_tables(cur, conn)

db.create_tables(cur, conn)

cur.execute("""INSERT INTO users (id, name, role, password) VALUES (1258, 'Владислав', 'worker', '1234')""")

visualizator.visualize_tables(cur)

db.disconnect(cur, conn)
