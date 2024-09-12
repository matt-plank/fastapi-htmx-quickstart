from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient):
    response = client.get("/healthcheck")

    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "ok"
