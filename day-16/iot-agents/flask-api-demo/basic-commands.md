# Create
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name": "Item1", "description": "First item"}'

# Read all
curl http://127.0.0.1:5000/items

# Read one
curl http://127.0.0.1:5000/items/1

# Update
curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "Updated description"}'

# Delete
curl -X DELETE http://127.0.0.1:5000/items/1
