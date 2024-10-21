from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from app.database.models.auth import AuthSession


class _AuthSessionRepo:
    """Manages access to AuthSession db objects."""

    def __init__(self, session: Session) -> None:
        """Initialise the repo with a db session."""
        self.session = session

    def find_by_token(self, token: str, must_be_valid: bool = True) -> AuthSession | None:
        """Find an auth session by its token."""
        found_token = self.session.query(AuthSession).filter_by(token=token).one_or_none()

        if found_token is None:
            return None

        if must_be_valid and not found_token.valid():
            return None

        return found_token


async def dependency(session: database.Session) -> _AuthSessionRepo:
    """FastAPI dependency to provide a db session to the repo."""
    return _AuthSessionRepo(session=session)


AuthSessionRepo = Annotated[_AuthSessionRepo, Depends(dependency)]
