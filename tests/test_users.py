# tests/test_users.py

from fastapi.testclient import TestClient
from users.run import app

client = TestClient(app)

def test_create_user(test_client):
    response = test_client.post("/users/", json={"name": "Juan Perez", "email": "juan@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "juan@example.com"


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_user():
    response = client.put("/users/1", json={"name": "Juan Actualizado", "email": "juan_actualizado@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Juan Actualizado"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
