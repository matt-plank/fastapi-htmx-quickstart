from typing import Callable, Literal

from fastapi.testclient import TestClient
from httpx import Response

HttpVerb = Literal["GET", "PUT", "POST", "DELETE"]


class RequestSequence:
    """Builder for sequences of tested requests, ideal for end-to-end testing."""

    def __init__(self, client: TestClient):
        """Initialise with FastAPI test client."""
        self.client = client
        self.action_lookup: dict[HttpVerb, Callable] = {
            "GET": self.client.get,
            "PUT": self.client.put,
            "POST": self.client.post,
            "DELETE": self.client.delete,
        }

    def then(
        self,
        method: HttpVerb,
        target: str,
        assert_status_code: int = 200,
        assert_contains: str | None = None,
        assert_cookie: str | None = None,
        **data,
    ):
        response: Response | None = None

        if method in ["PUT", "POST"]:
            response = self.action_lookup[method](target, data=data)
        else:
            response = self.action_lookup[method](target)

        assert response is not None

        assert response.status_code == assert_status_code
        assert assert_contains is None or assert_contains in response.text
        assert assert_cookie is None or assert_cookie in response.cookies

        for cookie in response.cookies:
            self.client.cookies.set(cookie, response.cookies[cookie])

        return self
