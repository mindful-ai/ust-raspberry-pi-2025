# 📡 Explanation: `@socketio.on("connect")` Handler in Flask-SocketIO

This document explains the purpose and functionality of the following Flask-SocketIO code block:

```python
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
```

---

## ✅ Purpose

This function is executed **automatically when a client connects** to the Flask-SocketIO server via a WebSocket.

It does the following:
1. Retrieves the **latest sensor data** from the SQLite3 database.
2. Sends this data to the **connected client** using Socket.IO.

---

## 🧠 Line-by-Line Explanation

### `@socketio.on("connect")`

- A **decorator** that tells Flask-SocketIO to run the following function when a new client connects via WebSocket.
- Triggered as soon as the browser loads the dashboard and establishes a Socket.IO connection.

---

### `def send_latest():`

- Defines the function that will execute on client connection.

---

### `conn = get_db_connection()`

- Opens a connection to the SQLite3 database.
- Uses a utility function defined in `database.py`.

---

### `latest = conn.execute(...).fetchone()`

- Executes a SQL query to retrieve the **latest sensor data** row.
- `ORDER BY id DESC LIMIT 1` ensures we get only the **most recent** row from the `sensor_data` table.

---

### `conn.close()`

- Closes the database connection after use to free resources.

---

### `if latest:`

- Checks whether any data was retrieved.
- Prevents errors if the database is empty (e.g., first-time startup).

---

### `socketio.emit("sensor_update", {...})`

- Emits the `sensor_update` event over WebSocket.
- Sends a dictionary with the latest temperature and pressure values.
- **All connected clients** listening for this event will receive the update.

---

## 🌐 What Happens in the Frontend?

In `dashboard.html`, the frontend is listening for the `sensor_update` event:

```javascript
socket.on("sensor_update", data => {
    document.getElementById("temp").innerText = data.temperature;
    document.getElementById("press").innerText = data.pressure;
});
```

So, when the client connects:
- The server runs `send_latest()`
- Emits the last stored sensor data
- The dashboard immediately displays the latest values

---

## 🔁 Summary

The `@socketio.on("connect")` handler:

- Ensures that clients **always see the most recent sensor data immediately**
- Enables **real-time synchronization** without needing to wait for the next MQTT message
- Is a key part of building responsive, real-time dashboards with Flask and Socket.IO

---
