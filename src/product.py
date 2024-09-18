class Product:
    name: str
    description: str
    price: float
    quantity: float

    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: float) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    def count_products(self) -> int:
        return self.product_count
