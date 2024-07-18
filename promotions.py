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
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * (quantity - quantity // 3)
