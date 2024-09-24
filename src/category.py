from typing import Any

from src.product import Product


class Category:

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Any]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def count_category(self) -> int:
        return self.category_count

    def add_product(self, product1: Product) -> Any:
        Category.product_count += 1
        self.__products.append(product1)

    def products_in_list(self):
        return self.__products

    @property
    def products(self) -> str:
        new_products = ""
        for i in self.__products:
            new_products += f"{str(i)}\n"
        return new_products
