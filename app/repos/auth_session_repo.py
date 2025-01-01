from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app import config, database
from app.database.models.auth import AuthSession


class _AuthSessionRepo:
    """Manages access to AuthSession db objects."""

    def __init__(self, session: Session) -> None:
        """Initialise the repo with a db session."""
        self.session = session

    def find_by_token(self, token: str, current_time: datetime) -> AuthSession | None:
        """Find an auth session by its token."""
        found_token = self.session.query(AuthSession).filter_by(token=token).one_or_none()

        if found_token is None:
            return None

        if not found_token.valid(current_time, config.MAX_AUTH_SESSION_AGE):
            return None

        return found_token


async def dependency(session: database.Session) -> _AuthSessionRepo:
    """FastAPI dependency to provide a db session to the repo."""
    return _AuthSessionRepo(session=session)


AuthSessionRepo = Annotated[_AuthSessionRepo, Depends(dependency)]

# Helps VS Code autocomplete types
__all__ = ("AuthSessionRepo",)
