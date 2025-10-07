from fastapi import APIRouter

from mars_probe_api.probes import views
from mars_probe_api.probes.responses import CreateProbeResponse

router = APIRouter()

router.post(
    "",
    summary="Lança a sonda e configura a malha",
    tags=["Probes"],
    name="create_probes",
    response_model=CreateProbeResponse,
)(views.CreateProbeView.post)
