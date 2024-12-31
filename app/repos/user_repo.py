from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from app.database.models.auth import PasswordHash
from app.database.models.users import User


class _UserRepo:
    """Manages access to users in the database."""

    def __init__(self, session: Session):
        """Initialise with db session."""
        self.session = session

    def new(self, email: str, password: str, created: datetime) -> User:
        """Create a new user."""
        password_hash = PasswordHash()
        password_hash.set(password)
        self.session.add(password_hash)

        user = User(email=email, created=created, password_hash=password_hash)
        self.session.add(user)

        self.session.commit()
        return user


async def dependency(session: database.Session):
    """FastAPI dependency."""
    return _UserRepo(session)


UserRepo = Annotated[_UserRepo, Depends(dependency)]

# Makes auto-complete easier for VS Code
__all__ = ("UserRepo",)
