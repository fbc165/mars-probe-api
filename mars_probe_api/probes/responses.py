from pydantic import BaseModel


class CreateProbeResponse(BaseModel):
    """
    Resposta padrão ao lançar sonda
    """

    id: str
    x: int
    y: int
    direction: str
