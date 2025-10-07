from fastapi import FastAPI

from mars_probe_api.probes.urls import router as probes_router

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

app.include_router(probes_router, prefix="/probes", tags=["Probes"])
