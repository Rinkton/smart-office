from prettytable import from_db_cursor
import db

def visualize_table(cur, table_name):
    print(table_name)
    cur.execute(f"select * from {table_name}")
    result = cur.fetchall()
    if cur.rowcount > 0:
        cur.execute(f"select * from {table_name}")
        x = from_db_cursor(cur)
        print(x)
    else:
        print("the table is empty")
    print()

def visualize_tables(cur):
    table_names = db.get_table_names(cur)
    for table_name in table_names:
        visualize_table(cur, table_name)