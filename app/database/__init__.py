from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session as SQLASession
from sqlalchemy.orm import sessionmaker

engine: Engine | None = None
SessionLocal = None


def init(database_url: str) -> None:
    """Initialise the database engine and session factory."""
    global engine
    global SessionLocal

    print("[database] Initialising database engine...")
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("[database] Done.")


async def dependency() -> AsyncGenerator[SQLASession, None]:
    """FastAPI dependency to retrieve database session."""
    global engine
    global SessionLocal

    assert engine is not None, "Engine should have been initialised by now"
    assert SessionLocal is not None, "SessionLocal should have been initialised by now"

    with SessionLocal() as session:
        yield session


Session = Annotated[SQLASession, Depends(dependency)]
