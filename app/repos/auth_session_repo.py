from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app import config, database
from app.database.models.auth import AuthSession
from app.database.models.users import User


class _AuthSessionRepo:
    """Manages access to AuthSession db objects."""

    def __init__(self, session: Session) -> None:
        """Initialise the repo with a db session."""
        self.session = session

    def new_for_user(self, user: User, current_time: datetime) -> AuthSession:
        """Create a new auth session for a user."""
        new_session = AuthSession(user_id=user.id, last_action=current_time)
        self.session.add(new_session)
        self.session.commit()
        return new_session

    def find_by_token(self, token: str, current_time: datetime) -> AuthSession | None:
        """Find an auth session by its token."""
        found_auth_session = self.session.query(AuthSession).filter_by(token=token).one_or_none()

        if found_auth_session is None:
            return None

        if found_auth_session.deactivated:
            return None

        if current_time - found_auth_session.last_action.replace(tzinfo=UTC) < config.MAX_AUTH_SESSION_AGE:
            return None

        return found_auth_session

    def remove(self, auth_session: AuthSession) -> None:
        """Remove an auth session from the database."""
        auth_session.deactivated = True
        self.session.commit()

    def set_last_action(self, auth_session: AuthSession, last_action: datetime) -> None:
        """Update the last action time of an auth session."""
        auth_session.last_action = last_action
        self.session.commit()


async def dependency(session: database.Session) -> _AuthSessionRepo:
    """FastAPI dependency to provide a db session to the repo."""
    return _AuthSessionRepo(session=session)


AuthSessionRepo = Annotated[_AuthSessionRepo, Depends(dependency)]

# Helps VS Code autocomplete types
__all__ = ("AuthSessionRepo",)
