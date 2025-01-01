from typing import Annotated

from fastapi import Cookie, Depends

from app.database.models.auth import AuthSession
from app.datetime_utils import CurrentTime
from app.repos.auth_session_repo import AuthSessionRepo


async def auth_session_from_token(
    auth_session_repo: AuthSessionRepo,
    current_time: CurrentTime,
    token: Annotated[str | None, Cookie(...)] = None,
) -> AuthSession | None:
    """Retrieve the auth session from a provided token cookie."""
    if token is None:
        return None

    found_auth_session = auth_session_repo.find_by_token(token, current_time)

    if found_auth_session is None:
        return None

    auth_session_repo.set_last_action(found_auth_session, current_time)

    return found_auth_session


AuthSessionFromToken = Annotated[AuthSession | None, Depends(auth_session_from_token)]

# Helps VS Code with autocompletion
__all__ = ("AuthSessionFromToken",)
