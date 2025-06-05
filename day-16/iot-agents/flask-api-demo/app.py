from flask import Flask, request, jsonify, abort
from database import get_db_connection, init_db

app = Flask(__name__)

@app.before_first_request
def setup():
    init_db()

@app.route("/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return jsonify(dict(item))

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Name is required")
    conn = get_db_connection()
    cursor = conn.execute("INSERT INTO items (name, description) VALUES (?, ?)",
                          (data["name"], data.get("description", "")))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_id, "name": data["name"], "description": data.get("description", "")}), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    if not data:
        abort(400, description="No data provided")
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if item is None:
        conn.close()
        abort(404)

    name = data.get("name", item["name"])
    description = data.get("description", item["description"])
    conn.execute("UPDATE items SET name = ?, description = ? WHERE id = ?",
                 (name, description, item_id))
    conn.commit()
    conn.close()
    return jsonify({"id": item_id, "name": name, "description": description})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db_connection()
    result = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        abort(404)
    return jsonify({"message": f"Item {item_id} deleted"})

if __name__ == "__main__":
    app.run(debug=True)
