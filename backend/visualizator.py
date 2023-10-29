from prettytable import from_db_cursor
import db

# TODO: After UPDATE the order of visualizing rows changing(recently updated go down, even if their id is lowest)

def visualize_table(cur, table_name):
    print(table_name)
    cur.execute(f"select * from {table_name}")
    print(from_db_cursor(cur))
    print()

def visualize_tables(cur):
    table_names = db.get_table_names(cur)
    for table_name in table_names:
        visualize_table(cur, table_name)
    print("End of visualizing")