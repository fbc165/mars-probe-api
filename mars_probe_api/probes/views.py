from fastapi import Depends, HTTPException, status

from mars_probe_api.probes.payloads import CreateProbePayload
from mars_probe_api.probes.responses import (
    CreateProbeResponse,
    ListProbesResponse,
    ProbeItem,
)
from mars_probe_api.probes.services import ProbeService
from mars_probe_api.store.mysqlstore import SQLAlchemySession, get_db


class CreateProbeView:
    @staticmethod
    def post(
        probe_setup: CreateProbePayload,
        db_session: SQLAlchemySession = Depends(get_db),
    ) -> CreateProbeResponse:
        """
        View responsável pelo lançamento de uma sonda
        Cria um sonda com sua posição atual, direção
        e define as dimensões do planalto/malha
        """

        try:
            probe = ProbeService.create_probe(
                terrain_length=probe_setup.x,
                terrain_width=probe_setup.y,
                direction=probe_setup.direction,
                db_session=db_session,
            )

            return CreateProbeResponse(
                id=probe.id, x=probe.x, y=probe.y, direction=probe.direction
            )
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_422_BAD_REQUEST, detail=str(e))

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )


class ListProbesView:
    @staticmethod
    def get(
        db_session: SQLAlchemySession = Depends(get_db),
    ) -> ListProbesResponse:
        """
        View responsável por listar todas as sondas lançadas
        """

        probes = ProbeService.get_all_probes(db_session=db_session)

        return ListProbesResponse(
            probes=[
                ProbeItem(id=probe.id, x=probe.x, y=probe.y, direction=probe.direction)
                for probe in probes
            ]
        )
