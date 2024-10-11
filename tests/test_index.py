from fastapi.testclient import TestClient

from tests.tools.request_sequence import RequestSequence


def test_end_to_end(client: TestClient):
    # fmt: off
    RequestSequence(client) \
        .then("GET", "/", assert_status_code=200, assert_contains="Hello") \
        .then("GET", "/healthcheck", assert_status_code=200, assert_contains="ok") \
        .then("GET", "/", assert_status_code=200, assert_contains="Hello")
    # fmt: on
