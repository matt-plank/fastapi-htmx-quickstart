import bcrypt
from sqlalchemy.types import String, TypeDecorator


class _PasswordHash:
    """Password type for storing hashed passwords."""

    def __init__(self, password_hash: bytes):
        """Initialise with a password hash."""
        self.password_hash = password_hash

    def verify(self, password: str) -> bool:
        """Verify a password against the hashed password."""
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash)


class PasswordHash(TypeDecorator):
    """Password type for storing hashed passwords."""

    impl = String

    def process_bind_param(self, value: str, dialect) -> str:
        """Set the value of the password field as the hash of the supplied password."""
        return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def process_result_value(self, value: str, dialect) -> _PasswordHash:
        """Retrieve the hashed password."""
        return _PasswordHash(value.encode("utf-8"))
