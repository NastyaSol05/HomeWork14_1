import pytest

from src.json_reader import read_json


@pytest.fixture
def json_read1() -> list:
    return read_json("../data/products.json")


def test_read_json(json_read1: list) -> None:
    assert json_read1[0].name == "Смартфоны"
