from typing import Any

from src.baseproduct import BaseProduct
from src.mixinprint import Mixinprint


class Product(BaseProduct, Mixinprint):
    """Класс с продуктами"""

    all_products: list = []
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: float) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            print("Товар с нулевым количеством не может быть добавлен")
            raise ValueError
        Product.product_count += 1
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if issubclass(type(other), type(self)):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError

    def count_products(self) -> int:
        """Метод, который считает количество продуктов"""
        return self.product_count

    @classmethod
    def new_product(cls, products_dict: dict) -> Any:
        """
        Метод, который проверяет дубликаты в продуктах и если они есть, меняет цену на большую и изменяет количество
        """
        for i in cls.all_products:
            if i.name == products_dict["name"]:
                i.quantity += products_dict["quantity"]
                if i.__price <= products_dict["price"]:
                    i.__price = products_dict["price"]
                    return i
        new_product = cls(
            products_dict["name"], products_dict["description"], products_dict["price"], products_dict["quantity"]
        )
        cls.all_products.append(new_product)
        return new_product

    @property
    def price(self) -> Any:
        """Геттер, который возвращает цену"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        """Сеттер, который дает изменять цену"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                answer_user = input(
                    "Введенная цена меньше прежней, вы уверены, что хотите поменять цену?\nЕсли да, нажмите y\n"
                )
                if answer_user == "y":
                    self.__price = new_price
