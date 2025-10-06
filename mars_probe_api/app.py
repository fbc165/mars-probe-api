from fastapi import FastAPI

app = FastAPI(
    title="Mars Probe API",
    description="API de controle de sondas em marte.",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Probes",
            "description": "Operações relacionadas a sonda em marte",
        },
    ],
)
