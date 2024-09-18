import pytest

from src.product import Product


@pytest.fixture
def count_products() -> Product:
    return Product("Banana", "Very tasty", 20, 200)


def test_quantity_products(count_products: Product) -> None:
    assert Product.product_count == 1
