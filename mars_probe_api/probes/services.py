from fastapi import Depends

from mars_probe_api.probes.models import Probe
from mars_probe_api.probes.payloads import DirectionEnum
from mars_probe_api.store.mysqlstore import SQLAlchemySession, get_db


class ProbeService:
    @classmethod
    def create_probe(
        cls,
        terrain_length: int,
        terrain_width: int,
        direction: DirectionEnum,
        session: SQLAlchemySession = Depends(get_db),
    ) -> Probe:
        probe = Probe(
            direction=direction.value,
            terrain_length=terrain_length,
            terrain_width=terrain_width,
        )
        session.add(probe)
        session.flush()

        return probe
