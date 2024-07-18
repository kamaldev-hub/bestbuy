from promotions import Promotion


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion: Promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def get_promotion(self) -> Promotion:
        return self.promotion

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def show(self) -> str:
        result = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            result += f", Promotion: {self.promotion.name}"
        return result

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Product is not active")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity")

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int) -> None:
        pass  # Ignores quantity changes

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Product is not active")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price

    def show(self) -> str:
        result = f"{self.name}, Price: {self.price}, Not in stock"
        if self.promotion:
            result += f", Promotion: {self.promotion.name}"
        return result


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Product is not active")
        if quantity > self.maximum:
            raise ValueError(f"Maximum purchase quantity exceeded (Maximum: {self.maximum})")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price

    def show(self) -> str:
        result = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
        if self.promotion:
            result += f", Promotion: {self.promotion.name}"
        return result
