from typing import Callable, Literal

from fastapi.testclient import TestClient
from httpx import Response

HttpVerb = Literal["GET", "PUT", "PATCH", "POST", "DELETE"]


class RequestSequence:
    """Builder for sequences of tested requests, ideal for end-to-end testing."""

    def __init__(self, client: TestClient):
        """Initialise with FastAPI test client."""
        self.client = client
        self.action_lookup: dict[HttpVerb, Callable] = {
            "GET": self.client.get,
            "PUT": self.client.put,
            "PATCH": self.client.patch,
            "POST": self.client.post,
            "DELETE": self.client.delete,
        }

    def then(
        self,
        method: HttpVerb,
        target: str,
        assert_status_code: int = 200,
        assert_contains: str | list[str] | None = None,
        assert_not_contains: str | list[str] | None = None,
        assert_cookie: str | None = None,
        assert_header: dict[str, str] | None = None,
        debug: bool = False,
        **data,
    ):
        response: Response | None = None

        if method in ["PUT", "POST"]:
            response = self.action_lookup[method](target, data=data)
        else:
            response = self.action_lookup[method](target)

        assert response is not None

        if debug:
            print(response.request.content.decode("utf-8"))
            print(response.text)

        assert response.status_code == assert_status_code, f"Expected {assert_status_code}, got {response.status_code}"

        if isinstance(assert_contains, list):
            for item in assert_contains:
                assert item in response.text, f"{item!r} not found in response text"
        elif isinstance(assert_contains, str):
            assert assert_contains in response.text, f"{assert_contains!r} not found in response text"

        if isinstance(assert_not_contains, list):
            for item in assert_not_contains:
                assert item not in response.text, f"{item!r} found in response text"
        elif isinstance(assert_not_contains, str):
            assert assert_not_contains not in response.text, f"{assert_not_contains!r} found in response text"

        assert assert_cookie is None or assert_cookie in response.cookies

        if assert_header is not None:
            for header in assert_header:
                assert header in response.headers, f"{header!r} not found in response headers"
                assert response.headers[header] == assert_header[header], f"Expected header {header!r} to be {assert_header[header]!r}, got {response.headers[header]!r}"

        for cookie in response.cookies:
            self.client.cookies.set(cookie, response.cookies[cookie])

        return self
