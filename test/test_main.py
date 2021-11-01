from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main_get_list():
    response = client.get("/contatos/?skip=0&limit=100")
    assert response.status_code == 200


def test_create_contato():
    response = client.post(
        "/contato/",
        json={
            "numerodetelefone": 651234,
            "nome": "65string1234",
            "sobrenome": "65string1234",
            "email": "65string1234@"
        },
    )
    assert response.status_code == 200



