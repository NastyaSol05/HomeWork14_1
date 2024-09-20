from typing import Any


class Product:
    all_products: list = []
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: float) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1

    def count_products(self) -> int:
        return self.product_count

    @staticmethod
    def new_product(products_dict: dict) -> Any:
        for i in Product.all_products:
            if i.name == products_dict["name"]:
                i.quantity += products_dict["quantity"]
                if i.__price <= products_dict["price"]:
                    i.__price = products_dict["price"]
                    return i
        new_product = Product(
            products_dict["name"], products_dict["description"], products_dict["price"], products_dict["quantity"]
        )
        Product.all_products.append(new_product)
        return new_product

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                answer_user = input(
                    "Введенная цена меньше прежней, вы уверены, что хотите поменять цену?\nЕсли да, нажмите y\n"
                )
                if answer_user == "y":
                    self.__price = new_price
