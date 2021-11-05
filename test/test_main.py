from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_get_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_main_get_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200


def test_main_get_list():
    response = client.get("/contatos/?skip=0&limit=100")
    assert response.status_code == 200


def test_main_get_contato():
    response = client.get("/contatos/10")
    assert response.status_code == 404
