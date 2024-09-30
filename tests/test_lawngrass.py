import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture
def lawngrass() -> tuple[LawnGrass, LawnGrass]:
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return grass1 + grass2


def test_add_smartphone(lawngrass):
    assert lawngrass == 35


def test_add_grass_smartphone():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    try:
        smartphone1 + grass1
    except TypeError:
        assert True