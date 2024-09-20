import json
from webbrowser import Error

from src.category import Category
from src.product import Product


def read_json(path: str) -> list:
    with open(path, "r") as f:
        data = json.load(f)
        all_category = []
        for i in data:
            try:
                all_products = []
                for j in i["products"]:
                    all_products.append(Product(j["name"], j["description"], j["price"], j["quantity"]))
                all_category.append(Category(i["name"], i["description"], all_products))
            except Error:
                print("Неверная структура")
        return all_category
