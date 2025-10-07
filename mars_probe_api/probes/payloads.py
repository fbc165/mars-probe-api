from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field, ValidationInfo, field_validator


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


class MoveProbePayload(BaseModel):
    commands: str

    @field_validator("commands")
    @classmethod
    def validate_command(cls, value: str, info: ValidationInfo) -> str:
        valid_commands = {command.value for command in CommandEnum}
        if not value:
            raise ValueError(f"empty command is not a valid movement")
        for command in value:
            if command not in valid_commands:
                raise ValueError(f"command '{command}' is not valid")

        return value
