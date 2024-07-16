from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
