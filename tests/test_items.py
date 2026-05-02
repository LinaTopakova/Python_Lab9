def test_create_item(client):
    response = client.post("/items/", json={"name": "Laptop", "price": 9.99})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 9.99
    assert "id" in data

def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"