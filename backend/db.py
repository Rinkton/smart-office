
def get_table_names(cur):
    cur.execute("""SELECT table_name FROM information_schema.tables""")
    table_names = []
    for table_name in cur:
        # Да, все это условия, чтобы избавиться в выводе от автоматически созданных таблиц..
        if table_name[0] == "collations":
            break
        if table_name[0][:2] != "pg":
            table_names.append(table_name[0])
    return table_names

def clear_table(cur, table_name):
    cur.execute(f"""DROP TABLE {table_name}""")

def clear_tables(cur):
    table_names = get_table_names(cur)
    for table_name in table_names:
        clear_table(cur, table_name)