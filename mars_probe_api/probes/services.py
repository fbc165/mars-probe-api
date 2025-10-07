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
        db_session: SQLAlchemySession,
    ) -> Probe:
        probe = Probe(
            direction=direction.value,
            terrain_length=terrain_length,
            terrain_width=terrain_width,
        )
        db_session.add(probe)
        db_session.flush()

        return probe

    @classmethod
    def get_all_probes(
        cls,
        db_session: SQLAlchemySession,
    ) -> list[Probe]:
        return db_session.query(Probe).order_by(Probe.id).all()

    @classmethod
    def get_probe_by_id(
        cls,
        id: str,
        db_session: SQLAlchemySession,
    ) -> Probe:
        return db_session.query(Probe).filter(Probe.id == id).one_or_none()
