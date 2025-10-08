import pytest

from mars_probe_api.probes.payloads import DirectionEnum

"""
Os testes foram realizados para uma sonda partindo da posição (0,0,NORTH)
A malha da sonda possui dimensões 5x5
"""


def test_probe_with_valid_movement(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição válida (1, 0, EAST)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "RM"}
    )

    response_data = response.json()

    assert response.status_code == 200
    assert response_data["id"] == probe_with_initial_position.id
    assert response_data["x"] == 1
    assert response_data["y"] == 0
    assert response_data["direction"] == DirectionEnum.EAST.value


def test_probe_with_invalid_movement_out_of_bound_left(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição inválida fora da malha (-1, 0, WEST)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "LM"}
    )

    assert response.status_code == 422


def test_probe_with_invalid_movement_out_of_bound_right(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição inválida fora da malha (6, 0, EAST)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "RMMMMMM"}
    )

    assert response.status_code == 422


def test_probe_with_invalid_movement_out_of_bound_up(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição inválida fora da malha (0, 6, NORTH)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "MMMMMM"}
    )

    assert response.status_code == 422


def test_probe_with_invalid_movement_out_of_bound_down(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição inválida fora da malha (0, -1, SOUTH)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "RRM"}
    )

    assert response.status_code == 422


def test_probe_with_valid_movement_more_than_one_spin(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição válida (0, 1, NORTH)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "RRRRM"}
    )

    response_data = response.json()

    assert response.status_code == 200
    assert response_data["id"] == probe_with_initial_position.id
    assert response_data["x"] == 0
    assert response_data["y"] == 1
    assert response_data["direction"] == DirectionEnum.NORTH.value


def test_probe_with_invalid_movement_more_than_one_spin(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição inválida fora da malha (0, -1, SOUTH)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "LLLLLLM"}
    )

    assert response.status_code == 422


def test_probe_with_valid_movement_after_displacement(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    """
    A sonda vai para uma posição válida (1, 2, EAST)
    """
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "MMRM"}
    )

    response_data = response.json()

    assert response.status_code == 200
    assert response_data["id"] == probe_with_initial_position.id
    assert response_data["x"] == 1
    assert response_data["y"] == 2
    assert response_data["direction"] == DirectionEnum.EAST.value


def test_probe_with_invalid_movement_after_displacement(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "MMLM"}
    )

    assert response.status_code == 422


def test_probe_with_invalid_command(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": "K"}
    )

    assert response.status_code == 422


def test_probe_with_empty_command(
    mock_get_probe_by_id, client, probe_with_initial_position
):
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"commands": ""}
    )

    assert response.status_code == 422


def test_probe_bad_payload(mock_get_probe_by_id, client, probe_with_initial_position):
    response = client.patch(
        f"/probes/{probe_with_initial_position.id}", json={"wrong_word": ""}
    )

    assert response.status_code == 422
