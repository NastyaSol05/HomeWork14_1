import pytest

from src.order import Order
from src.product import Product


@pytest.fixture
def one_order() -> Order:
    product1 = Product("Iphone 15", "512GB, Gray space", 500, 8)
    order1 = Order(product1, 3)
    return order1


def test_one_order(one_order: Order) -> None:
    assert one_order.product.quantity == 5
    assert one_order.total == 1500


def test_add_product_in_basket(one_order: Order) -> None:
    count = one_order.counter_product
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    one_order.add_product_in_basket(product1)
    assert one_order.counter_product == count + 1
