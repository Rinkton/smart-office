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

@app.route('/meeting_room/<id>', methods=['GET'])
def get_meeting_room(id):
    return jsonify({"message": f"Hello, {id}"})

@app.route('/meeting_room/<id>', methods=['POST'])
def take_meeting_room_time(id):
    data = request.json
    cur.execute(f"SELECT time FROM meeting_rooms WHERE id={id}")
    time = cur.fetchone()[0]
    no_time_intersections = len(time + data["time"]) == len(set(time + data["time"]))
    if no_time_intersections:
        new_time = sorted(time + data['time'])
        cur.execute(f"UPDATE meeting_rooms SET time = ARRAY {new_time} WHERE id={id}")
        return data, 201
    else:
        return jsonify({"message": "Это время уже занято"}), 404
@app.route('/v', methods=['GET'])
def visualize_please():
    global cur
    visualizator.visualize_tables(cur)
    return jsonify({"message": "visualized"}), 200

@app.route('/stationary', methods=['POST'])
def post_stationary_problem():
    """
    json должен иметь в себе user_id, type, amount, priority
    """
    if request.method == 'POST':
        req = request.get_json()
        cur.execute(
            f"""INSERT INTO stationary_problem (created_at, updated_at, user_id, type, amount, priority) VALUES (NOW(), NOW(), {req[0]}, {req[1]}, {req[2]}, {req[3]}, )""")

if __name__ == "__main__":
    cur, conn = db.connect()
    db.clear_tables(cur, conn)
    db.create_tables(cur, conn)
    cur.execute("INSERT INTO meeting_rooms (name, description, time) VALUES ('kat', 'fsafsg', ARRAY [5, 3])")
    cur.execute("INSERT INTO meeting_rooms (name, description, time) VALUES ('aba', 'fd', ARRAY [2, 3, 4])")
    visualizator.visualize_tables(cur)
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
