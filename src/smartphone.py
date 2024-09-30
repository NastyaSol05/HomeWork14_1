from src.product import Product


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: float,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.quantity + other.quantity
        raise TypeError