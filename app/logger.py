from datetime import datetime
from typing import Annotated, Any, Literal

from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from app.database.models.logging import Log
from app.datetime_utils import CurrentTime

LogEvent = Literal["AccountCreated", "AccountDeleted", "LogIn", "LogOut", "PageView"]


class _Logger:
    """Manages access to logs in the database."""

    def __init__(self, session: Session, current_time: datetime):
        """Initialise with db session."""
        self.session = session
        self.current_time = current_time

    def new(self, level: str, scope: str, **data: Any):
        log = Log(
            timestamp=self.current_time,
            level=level,
            scope=scope,
            data=data,
        )

        self.session.add(log)
        self.session.commit()

    def all(self, reversed: bool = False) -> list[Log]:
        query = self.session.query(Log)
        if reversed:
            return query.order_by(Log.timestamp.desc(), Log.id.desc()).all()
        return query.order_by(Log.timestamp.asc(), Log.id.asc()).all()

    def filtered_logs(
        self,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        scope: str | None = None,
        event: str | None = None,
        reversed: bool = False,
    ) -> list[Log]:
        query = self.session.query(Log)

        if start_time:
            query = query.filter(Log.timestamp >= start_time)

        if end_time:
            query = query.filter(Log.timestamp <= end_time)

        if scope:
            query = query.filter(Log.scope == scope)

        if event:
            query = query.filter(Log.data["event"].as_string() == event)

        if reversed:
            return query.order_by(Log.timestamp.desc(), Log.id.desc()).all()
        return query.order_by(Log.timestamp.asc(), Log.id.asc()).all()

    def info(self, scope: str, event: LogEvent, **data: Any):
        self.new("INFO", scope, event=event, **data)

    def warning(self, scope: str, event: str, **data: Any):
        self.new("WARNING", scope, event=event, **data)

    def error(self, scope: str, event: str, **data: Any):
        self.new("ERROR", scope, event=event, **data)


async def dependency(session: database.Session, current_time: CurrentTime):
    """FastAPI dependency."""
    return _Logger(session, current_time)


Logger = Annotated[_Logger, Depends(dependency)]

# Helps VS Code autocomplete types
__all__ = ("Logger",)
