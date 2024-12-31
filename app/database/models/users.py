from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base

if TYPE_CHECKING:
    from app.database.models.auth import PasswordHash


class User(Base):
    """Basic user model."""

    __tablename__ = "users"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    password_hash_id: Mapped[int] = mapped_column(ForeignKey("password_hashes.id"))

    email: Mapped[str]
    created: Mapped[datetime]

    # Relationships
    password_hash: Mapped["PasswordHash"] = relationship()
