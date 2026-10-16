import pytest

def average(values: list[float]) -> float:
    if not values:
        raise ValueError("A lista não pode estar vazia")
    return sum(values) / len(values)

def test_average_returns_mean():
    assert average([2, 4, 6]) == 4

def test_average_rejects_empty_list():
    with pytest.raises(ValueError):
        average([])
