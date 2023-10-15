import flask
from flask import request, jsonify, Flask

import db
import visualizator
from conv import time2str, date2str

app = Flask(__name__)


cur = None
conn = None

# убрать # из апп роута, условие сделать нормальным

def db_exec(what):
    """
    Функция, в которую поставляется строка, которая будет исполнена в Query Sql-я
    Прекрасно понимаю, что это небезопасно,
    но если что-то вдруг понадобится быстро сделать - неплохой вариант пока что
    """
    cur.execute(what)

@app.route('/rooms', methods=['GET'])
def get_rooms():
    if request.method == 'GET':
        cur.execute(
            f"""SELECT id, created_at, updated_at, description, seats_count FROM meeting_rooms""")
        jsone = jsonify(cur.fetchall())
        return jsone

@app.route('/stationary', methods=['POST'])
def post_stationary_problem():
    """
    json должен иметь в себе user_id, type, amount, priority
    """
    if request.method == 'POST':
        req = request.get_json()
        cur.execute(
            f"""INSERT INTO stationary_problem (created_at, updated_at, user_id, type, amount, priority) VALUES (NOW(), NOW(), {req[0]}, {req[1]}, {req[2]}, {req[3]}, )""")

'''
@app.route('/get_meeting_room', methods=['GET'])
def get_meeting_room(id):
    if request.method == 'GET':
        cur.execute(
            f"""SELECT id, meeting_roomsId, date, time FROM meeting_rooms_registration WHERE id={id}""")
        fetch = cur.fetchall()[0]
        if not fetch:
            return ""
        fetch = list(fetch)
        fetch[2] = date2str(fetch[2])
        fetch[3] = time2str(fetch[3])
        fetch = tuple(fetch)
        jsone = jsonify(fetch)
        return jsone

@app.route('/get_descriptions', methods=['GET'])
def get_descriptions():
    if request.method == 'GET':
        cur.execute("""SELECT * FROM meeting_rooms_description""")
        jsone = jsonify(cur.fetchall())
        return jsone

@app.route('/sign_up', methods=['POST'])
def sign_up(name, password):
    if request.method == 'POST':
      cur.execute(f"""INSERT INTO worker (name, password) VALUES ({name}, {password})""")

@app.route('/sign_in', methods=['GET'])
def sign_in(name, password):
  """
  Может вернуть 'неверный логин или пароль'
  """
  if request.method == 'GET':
    cur.execute(f"""SELECT * FROM worker WHERE name={name} AND password={password}""")
    if cur.fetchall()==None:
      return 'неверный логин или пароль'
    json = jsonify(cur.fetchall())
    return json

@app.route('/necessery', methods=['POST'])
def necessery(chancelleryId ,necessaryItem , quantity, levelOfUrgency ):
    if request.method == 'POST':
      cur.execute(f"""INSERT INTO chancellery (chancelleryId ,necessaryItem , quantity, levelOfUrgency) VALUES ({chancelleryId} ,{necessaryItem} , {quantity}, {levelOfUrgency})""")

@app.route('/pain', methods=['POST'])
def pain(painId, pain , levelOfUrgency ):
    if request.method == 'POST':
      cur.execute(f"""INSERT INTO pain (painId, pain , levelOfUrgency) VALUES ({painId}, {pain} , {levelOfUrgency})""")

@app.route('/register_meeting_room', methods=['POST'])
def register_meeting_room(id,meeting_roomsId, date, time):
    if request.method == 'POST':
      cur.execute(f"""INSERT INTO meeting_rooms_registration (id, meeting_roomsId, date, time) VALUES ({id}, {meeting_roomsId}, {date}, {time})""")
'''

if __name__ == "__main__":
    #app.run(debug=True)
    import testdata
    cur, conn = db.connect()
    db.create_tables(cur, conn)
    cur.execute(
        f"""INSERT INTO stationary_problems (created_at, updated_at, user_id, type, amount, priority) VALUES (NOW(), NOW(), 1, 'pen', 3, 'moderate')""")
    visualizator.visualize_tables(cur)
    testdata.create_test_data(cur)
    cur.execute("""SELECT * FROM meeting_rooms_description""")
    print(cur.fetchall() == None)


