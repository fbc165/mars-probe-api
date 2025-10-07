from mars_probe_api.probes.models import Probe
from mars_probe_api.probes.payloads import DirectionEnum
from mars_probe_api.store.mysqlstore import SQLAlchemySession


class ProbeService:
    @classmethod
    def create_probe(
        cls,
        terrain_length: int,
        terrain_width: int,
        direction: DirectionEnum,
        session: SQLAlchemySession,
    ) -> Probe:
        probe = Probe(
            direction=direction.value,
            terrain_length=terrain_length,
            terrain_width=terrain_width,
        )
        session.add(probe)
        session.flush()

        return probe

    @classmethod
    def get_all_probes(
        cls,
        session: SQLAlchemySession,
    ) -> list[Probe]:
        return session.query(Probe).order_by(Probe.id).all()
