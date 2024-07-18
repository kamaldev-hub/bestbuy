from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percentage / 100)


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        full_price_count = (quantity + 1) // 2
        half_price_count = quantity - full_price_count
        return (full_price_count * product.price) + (half_price_count * product.price / 2)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        regular_price_count = quantity - (quantity // 3)
        return product.price * regular_price_count
