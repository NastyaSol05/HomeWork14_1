from typing import Any, Iterator

from src.category import Category


class CategoryIterator:

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self.index < self.category.product_count:
            product = self.category.products_in_list()[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
