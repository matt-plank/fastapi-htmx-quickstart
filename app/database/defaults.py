import uuid
from datetime import UTC, datetime


def token() -> str:
    return str(uuid.uuid4())


def now() -> datetime:
    return datetime.now(UTC)
