import random
import uuid
from unittest import mock
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from mars_probe_api.probes.models import Probe
from mars_probe_api.probes.payloads import DirectionEnum
from mars_probe_api.store.mysqlstore import get_db

from ...app import app


class MockSession:
    def flush(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass


@pytest.fixture(scope="session", autouse=True)
def override_db_dependency():
    """
    Substitui a dependência get_db por uma sessão
    mock do db em todos os testes
    """

    def _get_mock_db():
        db_session = MockSession()
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = _get_mock_db
    yield
    app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def probe_with_initial_position() -> Probe:
    return Probe(
        id=str(uuid.uuid4()),
        x=0,
        y=0,
        direction=DirectionEnum.NORTH.value,
        terrain_length=5,
        terrain_width=5,
    )


@pytest.fixture
def probe_payload() -> dict:
    return {
        "x": 9,
        "y": 5,
        "direction": DirectionEnum.NORTH.value,
    }


@pytest.fixture
def probes_list() -> list[Probe]:
    return [
        Probe(
            id=str(uuid.uuid4()),
            x=random.choice([i for i in range(1, 100)]),
            y=random.choice([i for i in range(1, 100)]),
            direction=random.choice([d.value for d in DirectionEnum]),
            terrain_length=random.choice([i for i in range(1, 100)]),
            terrain_width=random.choice([i for i in range(1, 100)]),
        )
        for _ in range(2)
    ]


@pytest.fixture
def mock_get_probe_by_id(probe_with_initial_position):
    with mock.patch(
        "mars_probe_api.probes.services.ProbeService.get_probe_by_id"
    ) as mock_get_probe_by_id:
        mock_get_probe_by_id.return_value = probe_with_initial_position
        yield mock_get_probe_by_id


@pytest.fixture
def mock_create_probe(probe_payload):
    with mock.patch(
        "mars_probe_api.probes.services.ProbeService.create_probe"
    ) as mock_create_probe:
        mock_create_probe.return_value = Probe(
            id=str(uuid.uuid4()), x=0, y=0, direction=probe_payload["direction"]
        )
        yield mock_create_probe


@pytest.fixture
def mock_get_all_probes_two_items(probes_list):
    with mock.patch(
        "mars_probe_api.probes.services.ProbeService.get_all_probes"
    ) as mock_get_all_probes:
        mock_get_all_probes.return_value = probes_list
        yield mock_get_all_probes


@pytest.fixture
def mock_get_all_probes_no_items():
    with mock.patch(
        "mars_probe_api.probes.services.ProbeService.get_all_probes"
    ) as mock_get_all_probes:
        mock_get_all_probes.return_value = []
        yield mock_get_all_probes
