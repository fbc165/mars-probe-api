from uuid import UUID

import pytest

from mars_probe_api.probes.payloads import DirectionEnum

"""
O teste verifica a criação de uma sonda
"""


def test_create_probe_with_valid_payload(
    mock_create_probe,
    probe_payload,
    client,
):
    """
    Lançamento válido de uma sonda
    """
    response = client.post(
        f"/probes",
        json={
            "x": probe_payload["x"],
            "y": probe_payload["y"],
            "direction": probe_payload["direction"],
        },
    )

    response_data = response.json()

    assert isinstance(response_data["id"], str)
    assert response_data["x"] == 0
    assert response_data["y"] == 0
    assert response_data["direction"] == probe_payload["direction"]


def test_create_probe_with_invalid_direction(
    mock_create_probe,
    probe_payload,
    client,
):
    """
    Lançamento inválido de uma sonda
    """
    response = client.post(
        f"/probes",
        json={
            "x": 5,
            "y": 5,
            "direction": "INVALID",
        },
    )

    assert response.status_code == 422


def test_create_probe_with_invalid_x(
    mock_create_probe,
    probe_payload,
    client,
):
    """
    Lançamento inválido de uma sonda
    """
    response = client.post(
        f"/probes",
        json={
            "x": -5,
            "y": 5,
            "direction": DirectionEnum.NORTH.value,
        },
    )

    assert response.status_code == 422


def test_create_probe_with_invalid_y(
    mock_create_probe,
    probe_payload,
    client,
):
    """
    Lançamento inválido de uma sonda
    """
    response = client.post(
        f"/probes",
        json={
            "x": 5,
            "y": -5,
            "direction": DirectionEnum.NORTH.value,
        },
    )

    assert response.status_code == 422
