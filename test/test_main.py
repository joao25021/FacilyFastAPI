from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_main_get_list():
    response = client.get("/contatos")
    assert response.status_code == 200


def test_create_contato():
    response = client.post(
        "/",
        json={
            "numerodetelefone": 651234,
            "nome": "65string1234",
            "sobrenome": "65string1234",
            "email": "65string1234@"
        },
    )
    assert response.status_code == 200



