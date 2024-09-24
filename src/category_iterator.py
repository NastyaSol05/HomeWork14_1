from src.category import Category
from src.product import Product


class CategoryIterator:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.category.product_count:
            product = self.category.products_in_list()[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
