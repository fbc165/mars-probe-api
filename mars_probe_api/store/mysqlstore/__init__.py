from typing import Generator

from mars_probe_api.settings import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SQLAlchemySession
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_size=30,
    max_overflow=15,
    pool_recycle=1800,
    echo=False,
    connect_args={
        "charset": "utf8mb4",
        "autocommit": False,
    },
)
Session = sessionmaker(bind=engine)


def get_db() -> Generator[SQLAlchemySession, None, None]:
    """
    Dependency para injeção de dependência do FastAPI
    """
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
