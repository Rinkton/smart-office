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

def create_tables(cur):
    """
    Создает все нужные нам таблички
    """
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id serial PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    role VARCHAR(255)
    )
    """)

    cur.execute("""CREATE TYPE stationary_type AS ENUM ('pen', 'pencil', 'eraser', 'ruler', 'scissors', 'glue', 'stapler', 'paper_clips', 'binder_clips', 'sticky_note', 'highlighter', 'tape', 'calculator', 'notebook', 'folder', 'index_cards', 'push_pins', 'rubber_bands', 'whiteboard_markers', 'correction_fluid');""")
    cur.execute("""CREATE TYPE status_type AS ENUM ('online', 'away', 'dinner', 'smoking', 'busy', 'do_not_disturb', 'offline')""")
    cur.execute("""CREATE TYPE priority_type AS ENUM ('irrelevant', 'moderate', 'critical')""")
    cur.execute("""CREATE TABLE IF NOT EXISTS stationary_problems (
    id serial PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    user_id INTEGER REFERENCES users(id),
    type stationary_type,
    amount INT,
    priority priority_type
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS meeting_rooms (
    id serial PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    description VARCHAR(255),
    seats_count INT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS meeting_rooms_booking (
    id serial PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    user_id INTEGER REFERENCES users(id),
    room_id INT,
    time INT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS user_statuses (
    id serial PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    user_id INTEGER REFERENCES users(id),
    status status_type
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS office_problems (
        id serial PRIMARY KEY,
        created_at TIMESTAMP DEFAULT NOW(),
        updated_at TIMESTAMP DEFAULT NOW(),

        user_id INTEGER REFERENCES users(id),
        message VARCHAR(2000),
        priority priority_type
        )""")
