from typing import Any

from src.basecategory import BaseCategory
from src.exceptions import ZeroQuantityProduct
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
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Товар с нулевым количеством не может быть добавлен.")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Продукт был успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")

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

    def middle_price(self) -> float:
        try:
            return float(sum([product.price for product in self.products_in_list()]) / len(self.products_in_list()))
        except ZeroDivisionError:
            return 0
