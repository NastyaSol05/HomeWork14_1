import json
import os
from webbrowser import Error

from src.category import Category
from src.product import Product


def read_json(path: str) -> list:
    """Функция, которая открывает json file и создает список продуктов"""
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), path)), "r") as f:
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
