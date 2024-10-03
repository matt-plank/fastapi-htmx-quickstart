import bcrypt
from sqlalchemy.orm import Mapped, mapped_column

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
