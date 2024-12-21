import uuid
from datetime import datetime, timedelta

import bcrypt
from sqlalchemy.orm import Mapped, mapped_column

from app import config
from app.database.models.base import Base


class PasswordHash(Base):
    """Represents a hashed password in the database."""

    __tablename__ = "password_hashes"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    password_hash: Mapped[str]

    def set(self, new_password: str) -> None:
        """Set the hashed password."""
        self.password_hash = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify(self, password: str) -> bool:
        """Verify the password."""
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash.encode("utf-8"))


class AuthSession(Base):
    """Temporary auth sessions for website login."""

    __tablename__ = "auth_session"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(default=lambda: str(uuid.uuid4()))
    last_action: Mapped[datetime]

    def valid(self, current_time: datetime, max_auth_session_age: timedelta) -> bool:
        """Check if the session is still valid."""
        return current_time - self.last_action < max_auth_session_age
