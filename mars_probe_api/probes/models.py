import uuid
from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base  # type: ignore

Base: Any = declarative_base()


class Probe(Base):
    __tablename__ = "probes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    x = Column(Integer, nullable=False, default=0)
    y = Column(Integer, nullable=False, default=0)
    direction = Column(String(10), nullable=False)
    terrain_length = Column(Integer, nullable=False)
    terrain_width = Column(Integer, nullable=False)
