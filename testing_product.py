import pytest
from products import Product


def test_normal_product_creation():
    product = Product("Test Product", price=10, quantity=100)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 100
    assert product.active == True


def test_invalid_product_creation():
    with pytest.raises(ValueError):
        Product("", price=10, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("Test Product", price=-10, quantity=100)  # Negative price


def test_product_becomes_inactive():
    product = Product("Test Product", price=10, quantity=1)
    product.buy(1)
    assert product.active == False


def test_product_purchase():
    product = Product("Test Product", price=10, quantity=10)
    total_price = product.buy(3)
    assert product.quantity == 7
    assert total_price == 30


def test_buy_larger_quantity_than_exists():
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)
