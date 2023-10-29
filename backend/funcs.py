from flask import request, jsonify, Flask

import db
import visualizator
from conv import time2str, date2str


app = Flask(__name__)

cur = None
conn = None


@app.route('/meeting_room', methods=['GET'])
def get_meeting_rooms():
    cur.execute(f"SELECT id, name, description FROM meeting_rooms")
    fetch = cur.fetchall()
    meeting_rooms = []
    for x in fetch:
        meeting_room = {
            "id": x[0],
            "name": x[1],
            "description": x[2],
        }
        meeting_rooms.append(meeting_room)
    return jsonify(meeting_rooms)

@app.route('/meeting_room/<id>', methods=['GET'])
def get_meeting_room(id):
    cur.execute(f"SELECT id, name, description, time FROM meeting_rooms WHERE id={id}")
    fetch = cur.fetchone()
    if fetch == None:
        return jsonify({"message": f"Переговорки с id {id} не было найдено"}), 404
    meeting_room = {
        "id": fetch[0],
        "name": fetch[1],
        "description": fetch[2],
        "time": fetch[3],
    }
    return jsonify(meeting_room)

@app.route('/meeting_room/<id>', methods=['POST'])
def post_meeting_room_time(id):
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

@app.route('/meeting_room/<id>', methods=['DELETE'])
def delete_meeting_room_time(id):
    data = request.json
    cur.execute(f"SELECT time FROM meeting_rooms WHERE id={id}")
    time = cur.fetchone()[0]
    for t in data["time"]:
        try:
            time.remove(t)
        except ValueError:
            pass
    if len(time) > 0:
        cur.execute(f"UPDATE meeting_rooms SET time = ARRAY {time} WHERE id={id}")
    else: # По какой-то причине я не могу просто дать пустой массив, требует тип массива, который я не знаю как указать
        # Посему приходится вводить этот if-else
        cur.execute(f"UPDATE meeting_rooms SET time = ARRAY[]::integer[] WHERE id={id}")
    return data, 200

@app.route('/v', methods=['GET'])
def visualize_please():
    global cur
    visualizator.visualize_tables(cur)
    return jsonify({"message": "visualized"}), 200

if __name__ == "__main__":
    cur, conn = db.connect()
    db.clear_tables(cur, conn)
    db.create_tables(cur, conn)
    cur.execute("INSERT INTO meeting_rooms (name, description, time) VALUES ('kat', 'fsafsg', ARRAY [5, 3])")
    cur.execute("INSERT INTO meeting_rooms (name, description, time) VALUES ('aba', 'fd', ARRAY [2, 3, 4])")
    visualizator.visualize_tables(cur)
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
