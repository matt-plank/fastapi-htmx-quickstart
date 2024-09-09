import bcrypt
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Login(Base):
    """Basic user model."""

    __tablename__ = "users"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    _password_hash: Mapped[str]

    def set_password(self, password: str) -> None:
        """Set the password for the user."""
        salt = bcrypt.gensalt()
        self._password_hash = bcrypt.hashpw(password.encode(), salt).decode()

    def check_password(self, password: str) -> bool:
        """Check if the password is correct."""
        return bcrypt.checkpw(password.encode(), self._password_hash.encode())
