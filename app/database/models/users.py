from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base
from app.database.models.password import PasswordHash


class Login(Base):
    """Basic user model."""

    __tablename__ = "users"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password_hash_id: Mapped[int] = mapped_column(ForeignKey("password_hashes.id"))

    # Relationships
    password_hash: Mapped[PasswordHash] = relationship()
