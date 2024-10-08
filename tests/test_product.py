from typing import Any

import pytest

from src.product import Product


@pytest.fixture
def count_products() -> Product:
    Product.product_count = 0
    return Product("Banana", "Very tasty", 20, 200)


@pytest.fixture
def products() -> Any:
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture
def add_products() -> Any:
    product1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 1.0,
            "quantity": 5,
        }
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 1.0, 8)
    return product1 + product2


def test_quantity_products(count_products: Product) -> None:
    assert Product.product_count == 1


def test_new_products(products: Any) -> None:
    assert products.name == "Samsung Galaxy S23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_price(products: Any) -> None:
    products.price = -100
    assert products.price == 180000.0


def test_add(add_products: dict) -> None:
    assert add_products == 13.0
