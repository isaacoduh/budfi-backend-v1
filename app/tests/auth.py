from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/v1/login", json={"username": "test_user", "password": "password"})
    assert response.status_code == 200