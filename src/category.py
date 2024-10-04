from typing import Any

from src.basecategory import BaseCategory
from src.product import Product


class Category(BaseCategory):
    """Класс с категориями"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Any]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        summ = 0
        for i in self.__products:
            summ += i.quantity
        return f"{self.name}, количество продуктов: {summ} шт."

    def count_category(self) -> int:
        """Метод, для подсчета категорий"""
        return self.category_count

    def add_product(self, product: Any) -> Any:
        """Метод, который добавляет продукты в категорию"""
        if not issubclass(type(product), Product):
            raise TypeError
        Category.product_count += 1
        self.__products.append(product)

    def products_in_list(self) -> list:
        """Метод, который возвращает список продуктов"""
        return self.__products

    @property
    def products(self) -> str:
        """Геттер, который возвразает продукты в формате "Имя продукта, количество продуктов: n шт." """
        new_products = ""
        for i in self.__products:
            new_products += f"{str(i)}\n"
        return new_products
