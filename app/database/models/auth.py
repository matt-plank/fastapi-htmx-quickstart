import uuid
from datetime import datetime
from typing import TYPE_CHECKING

import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base

if TYPE_CHECKING:
    from app.database.models.users import User


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

    __tablename__ = "auth_sessions"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))

    token: Mapped[str] = mapped_column(default=lambda: str(uuid.uuid4()))
    deactivated: Mapped[bool] = mapped_column(default=False)
    last_action: Mapped[datetime]

    # Relationships
    user: Mapped["User | None"] = relationship(back_populates="auth_sessions")
