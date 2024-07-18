from promotions import Promotion, BuyTwoGetOneFree


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
            # For "Buy 2, Get 1 Free" promotion
            if isinstance(self.promotion, BuyTwoGetOneFree):
                actual_quantity = quantity + (quantity // 2)
            else:
                actual_quantity = quantity
        else:
            total_price = self.price * quantity
            actual_quantity = quantity

        self.quantity -= actual_quantity  # Reduce the stock by the actual quantity

        if self.quantity == 0:
            self.active = False

        return total_price

    def set_promotion(self, promotion: Promotion) -> None:
        self.promotion = promotion


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited{promotion_info}"

    def buy(self, quantity: int) -> float:
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}{promotion_info}"

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} items at once")
        return super().buy(quantity)