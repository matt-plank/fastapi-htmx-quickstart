from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base
from app.database.types.password_hash import PasswordHash


class Login(Base):
    """Basic user model."""

    __tablename__ = "users"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password_hash: Mapped[PasswordHash]
