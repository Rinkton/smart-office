def create_test_data(cur):
    cur.execute("""INSERT INTO users (name, role, password) VALUES ('Bob', 'worker', '1234')""")
    cur.execute("""INSERT INTO users (name, role, password) VALUES ('Kay', 'worker', '5678')""")
    cur.execute("""INSERT INTO users (name, role, password) VALUES ('Jean', 'admin', '1234')""")
    cur.execute("""INSERT INTO pain (painful_user, pain, levelOfUrgency) VALUES (1, 'folder', 2)""")
    cur.execute("""INSERT INTO pain (painful_user, pain, levelOfUrgency) VALUES (2, 'tape', 3)""")
    cur.execute("""INSERT INTO pain (painful_user, pain, levelOfUrgency) VALUES (2, 'folder', 4)""")
    cur.execute("""INSERT INTO meeting_rooms_description (description) VALUES ('desc')""")
    cur.execute("""INSERT INTO meeting_rooms_description (description) VALUES ('desc2')""")
