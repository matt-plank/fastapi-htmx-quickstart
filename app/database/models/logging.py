from datetime import datetime
from typing import Any

from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Log(Base):
    __tablename__ = "logs"

    # DB Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime]
    level: Mapped[str]
    scope: Mapped[str]
    data: Mapped[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "level": self.level,
            "scope": self.scope,
            **self.data,
        }
