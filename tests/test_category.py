import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def count_category() -> Category:
    return Category("fruits", "Fresh and sweet fruits", ["banana", "Banana2"])


@pytest.fixture
def category() -> Category:
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    return category1


@pytest.fixture
def category_middle() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category2 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    return category2


def test_category_count(count_category: Category) -> None:
    assert Category.category_count == 1


def test_add_product(category: Category) -> None:
    count = category.product_count
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category.add_product(product1)
    assert category.product_count == count + 1


def test_products(category: Category) -> None:
    product2 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category.add_product(product2)
    assert category.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_middle_price(category: Category) -> None:
    assert category.middle_price() == 0


def test_middle_price_2(category_middle: Category) -> None:
    assert category_middle.middle_price() == 140333.33333333334
