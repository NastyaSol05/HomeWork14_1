from src.product import Product


class Order:

    total: float

    def __init__(self, product: Product, counter_product: int) -> None:
        self.product = product
        self.counter_product = counter_product
        self.total = self.product.price * counter_product
        self.product.quantity -= counter_product

    def __str__(self) -> str:
        return (
            f"В вашем заказе {self.product.name} в количестве {self.counter_product} шт., Итоговая сумма: {self.total}"
        )


product1 = Product("Iphone 15", "512GB, Gray space", 500, 8)
order1 = Order(product1, 2)
print(order1)
