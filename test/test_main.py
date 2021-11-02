from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_get_list():
    response = client.get("/contatos/?skip=0&limit=100")
    assert response.status_code == 200






