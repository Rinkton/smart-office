import psycopg2

def connect():
    """
    Подключает к БД и возвращает курсор
    """
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234567890", port=5432)
    cur = conn.cursor()
    return cur, conn

def disconnect(cur, conn):
    conn.commit()
    cur.close()
    conn.close()

def get_table_names(cur):
    cur.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    fetch = cur.fetchall() # [('meeting_rooms', ), ('worker', )]
    table_names = []
    for f in fetch:
        table_names.append(f[0])
    return table_names

def clear_table(cur, conn, table_name):
    conn.commit() # Чтобы если мы роллбэкнемся, то откатился только дроп, а не всё, что ранее ещё делали
    try:
        cur.execute(f"""DROP TABLE {table_name}""")
    except:
        # Если какая-то ошибка произошла, то возможна это из-за того,
        # что таблица связана и её дропать через CASCADE надо
        conn.rollback() # Избавляемся от ошибок от неудачного исполнения
        cur.execute(f"""DROP TABLE {table_name} CASCADE""")

def clear_tables(cur, conn):
    table_names = get_table_names(cur)
    for table_name in table_names:
        clear_table(cur, conn, table_name)