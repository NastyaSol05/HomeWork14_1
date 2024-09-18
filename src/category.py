class Category:

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def count_category(self) -> int:
        return self.category_count

    def product_list(self) -> list:
        return self.products
