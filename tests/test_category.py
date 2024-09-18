import pytest

from src.category import Category


@pytest.fixture
def count_category() -> Category:
    return Category("fruits", "Fresh and sweet fruits", ["banana"])


def test_category_count(count_category: Category) -> None:
    assert Category.category_count == 1
