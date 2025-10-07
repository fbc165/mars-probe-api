from fastapi import APIRouter

from mars_probe_api.probes import views
from mars_probe_api.probes.responses import CreateProbeResponse, ListProbesResponse

router = APIRouter()

router.post(
    "",
    summary="Lança a sonda e configura a malha",
    tags=["Probes"],
    name="create_probes",
    response_model=CreateProbeResponse,
)(views.CreateProbeView.post)

router.get(
    "",
    summary="Lista sondas",
    tags=["Probes"],
    name="list_probes",
    response_model=ListProbesResponse,
)(views.ListProbesView.get)
