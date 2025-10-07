from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class DirectionEnum(str, Enum):
    """
    Direções possíveis de uma sonda
    Ordenadas no sentido horário
    """

    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


class CommandEnum(str, Enum):
    """
    Comandos válidos para movimentar a sonda
    """

    TURN_LEFT = "L"
    TURN_RIGHT = "R"
    MOVE_FORWARD = "M"


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
