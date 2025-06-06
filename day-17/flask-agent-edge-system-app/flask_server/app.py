import eventlet
eventlet.monkey_patch()

from flask import Flask, request, render_template
from flask_socketio import SocketIO
from database import get_db_connection, init_db


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.before_first_request
def setup():
    init_db()

@app.route("/")
def index():
    conn = get_db_connection()
    latest = conn.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return render_template("dashboard.html", latest=latest)

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    temperature = data.get("temperature")
    pressure = data.get("pressure")

    conn = get_db_connection()
    conn.execute("INSERT INTO sensor_data (temperature, pressure) VALUES (?, ?)",
                 (temperature, pressure))
    conn.commit()
    conn.close()

    socketio.emit("sensor_update", data)
    return {"status": "stored and emitted"}, 200

@socketio.on("connect")
def send_latest():
    conn = get_db_connection()
    latest = conn.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    if latest:
        socketio.emit("sensor_update", {
            "temperature": latest["temperature"],
            "pressure": latest["pressure"]
        })

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
