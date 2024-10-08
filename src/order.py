from typing import Any

from src.basecategory import BaseCategory
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Order(BaseCategory):

    total: float
    product_list: list = []

    def __init__(self, product: Product, counter_product: int) -> None:
        self.product = product
        self.counter_product = counter_product
        self.total = self.product.price * counter_product
        self.product.quantity -= counter_product

    def __str__(self) -> str:
        return (
            f"В вашем заказе {self.product.name} в количестве {self.counter_product} шт., Итоговая сумма: {self.total}"
        )

    def add_product_in_basket(self, product: Any) -> Any:
        """Метод, который добавляет продукты в корзину"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Товар с нулевым количеством не может быть добавлен.")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.product_list.append(product)
                self.counter_product += 1
                print("Продукт был успешно добавлен в корзину.")
            finally:
                print("Обработка добавления товара завершена.")
