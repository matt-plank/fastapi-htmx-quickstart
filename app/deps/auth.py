from typing import Annotated

from fastapi import Cookie, Depends

from app.database.models.auth import AuthSession
from app.repos.auth_session_repo import AuthSessionRepo


async def auth_session_from_token(
    auth_session_repo: AuthSessionRepo,
    token: Annotated[str | None, Cookie(...)] = None,
) -> AuthSession | None:
    """Retrieve the auth session from a provided token cookie."""
    if token is None:
        return None

    return auth_session_repo.find_by_token(token)


AuthSessionFromToken = Annotated[AuthSession | None, Depends(auth_session_from_token)]
