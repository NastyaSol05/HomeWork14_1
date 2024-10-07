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
