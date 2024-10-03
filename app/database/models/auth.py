from datetime import datetime

import bcrypt
from sqlalchemy.orm import Mapped, mapped_column

from app import config
from app.database import defaults
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
    token: Mapped[str] = mapped_column(default=defaults.token)
    last_action: Mapped[datetime] = mapped_column(default=defaults.now)

    def valid(self) -> bool:
        """Check if the session is still valid."""
        return defaults.now() - self.last_action < config.MAX_AUTH_SESSION_AGE
