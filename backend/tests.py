import unittest
import db
import funcs
# ВНИМАНИЕ! При запуске этого скрипта все таблицы чистятся!


def _in():
    """
    Создаёт подключения, создаёт Funcs объект, чистит и создаёт вновь таблицы
    """
    cur, conn = db.connect()
    funcs.cur = cur
    funcs.conn = conn
    db.clear_tables(cur, conn)
    db.create_tables(cur)
    return cur, conn


def _out(cur, conn):
    """
    Заканчивает тест
    """
    db.disconnect(cur, conn)

class MyTestCase(unittest.TestCase):

    def test_get_meeting_room(self):
        cur, conn = _in() #f"""SELECT id, meeting_roomsId, date, time FROM meeting_rooms_registration WHERE id={id}""")

        # arrange
        cur.execute("""INSERT INTO meeting_rooms_description (description) VALUES ('desc')""")
        cur.execute("""INSERT INTO meeting_rooms_registration (meeting_roomsId, date, time) VALUES (1, '2017/09/05', '16:13:10')""")

        # act

        json = funcs.get_meeting_room(1)

        # assert
        _out(cur, conn)
        self.assertEqual(json, '[1, 1, "2017:9:5", "16:13:10"]')


if __name__ == '__main__':
    unittest.main()
