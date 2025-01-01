from typing import Generator

from fastapi.testclient import TestClient
from pytest import fixture

from app import database
from app.app import app
from app.database.models import Base


@fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        assert database.engine is not None
        Base.metadata.create_all(bind=database.engine)
        yield c
        Base.metadata.drop_all(bind=database.engine)
