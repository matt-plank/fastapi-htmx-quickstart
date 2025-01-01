from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends


def current_time() -> datetime:
    return datetime.now(UTC)


CurrentTime = Annotated[datetime, Depends(current_time)]

# Helps VS Code autocomplete types
__all__ = ("CurrentTime",)
