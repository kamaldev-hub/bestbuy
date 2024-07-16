class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise Exception("Insufficient quantity")
        if not self.active:
            raise Exception("Product is not active")
        self.quantity -= quantity
        return quantity * self.price