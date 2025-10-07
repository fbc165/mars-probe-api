from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class DirectionEnum(str, Enum):
    """
    Direções possíveis de uma sonda
    """

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


# Tipos personalizados

Coordinate = Annotated[
    int, Field(gt=0)
]  # Representa valores possíveis para uma coordenada da sonda


class CreateProbePayload(BaseModel):
    """
    Payload para lançar uma sonda e configurar a malha
    """

    x: Coordinate
    y: Coordinate
    direction: DirectionEnum
