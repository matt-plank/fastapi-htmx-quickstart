from typing import Generator

from fastapi.testclient import TestClient
from pytest import fixture

from app.app import app


@fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
