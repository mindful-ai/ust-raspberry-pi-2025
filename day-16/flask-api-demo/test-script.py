import requests

BASE_URL = "http://127.0.0.1:5000/items"
headers = {"Content-Type": "application/json"}

def test_create_item():
    payload = {"name": "Item1", "description": "First item"}
    response = requests.post(BASE_URL, json=payload, headers=headers)
    print("CREATE:", response.status_code, response.json())

def test_read_all_items():
    response = requests.get(BASE_URL)
    print("READ ALL:", response.status_code, response.json())

def test_read_single_item(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}")
    print("READ ONE:", response.status_code, response.json())

def test_update_item(item_id):
    payload = {"name": "Updated Item", "description": "Updated description"}
    response = requests.put(f"{BASE_URL}/{item_id}", json=payload, headers=headers)
    print("UPDATE:", response.status_code, response.json())

def test_delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}")
    print("DELETE:", response.status_code, response.text)

if __name__ == "__main__":
    test_create_item()
    test_read_all_items()
    test_read_single_item(1)
    test_update_item(1)
    test_read_single_item(1)
    test_delete_item(1)
    test_read_all_items()
