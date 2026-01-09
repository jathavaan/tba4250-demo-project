from typing import Any, Generator

from sqlmodel import Session
from app.core import engine


def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
