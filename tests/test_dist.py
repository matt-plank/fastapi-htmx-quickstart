from fastapi.testclient import TestClient


def test_tailwind(client: TestClient):
    response = client.get("/static/dist/tailwind.css")

    assert response.status_code == 200
    assert "tailwindcss" in response.text


def test_bundle(client: TestClient):
    response = client.get("/static/dist/bundle.js")

    assert response.status_code == 200
    assert "(()=>{" in response.text
