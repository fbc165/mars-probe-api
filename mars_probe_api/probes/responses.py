from pydantic import BaseModel


class CreateProbeResponse(BaseModel):
    """
    Resposta padrão ao lançar sonda
    """

    id: str
    x: int
    y: int
    direction: str


class ProbeItem(BaseModel):
    """
    Dados retornados na listagem das sondas
    """

    id: str
    x: int
    y: int
    direction: str


class ListProbesResponse(BaseModel):
    """
    Lista todas as sondas lançadas
    """

    probes: list[ProbeItem]
