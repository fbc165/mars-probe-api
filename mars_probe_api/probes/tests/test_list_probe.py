import pytest

"""
O teste verifica se a listagem das sondas segue o padrão
"""


def test_list_with_multiple_probes(
    mock_get_all_probes_two_items,
    client,
):
    """
    Listagem todas as sondas lançadas
    """
    response = client.get(f"/probes")

    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data["probes"]) == 2
    assert isinstance(response_data["probes"], list)


def test_list_with_no_probes(
    mock_get_all_probes_no_items,
    client,
):
    """
    Listagem no caso de não haver sondas lançadas
    """
    response = client.get(f"/probes")

    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data["probes"]) == 0
    assert isinstance(response_data["probes"], list)
