from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondHalfPrice, BuyTwoGetOneFree
from store import Store


def start(store):
    while True:
        print("\nStore Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == '1':
            products = store.get_all_products()
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.show()}")

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == '3':
            order_list = []
            while True:
                # Only get products that are in stock
                in_stock_products = [p for p in store.get_all_products() if p.quantity > 0]

                if not in_stock_products:
                    print("Sorry, all products are out of stock.")
                    break

                for i, product in enumerate(in_stock_products, 1):
                    print(f"{i}. {product.show()}")

                print("\nWhen you want to finish order, enter empty text.")
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break

                try:
                    product_index = int(product_choice) - 1
                    if 0 <= product_index < len(in_stock_products):
                        product = in_stock_products[product_index]
                        quantity = int(input("What amount do you want? "))
                        if quantity <= 0:
                            print("Please enter a positive quantity.")
                        elif quantity > product.quantity:
                            print(f"Sorry, we only have {product.quantity} in stock.")
                        else:
                            order_list.append((product, quantity))
                            print("Product added to list!")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if order_list:
                try:
                    total_price = store.order(order_list)
                    print(f"Order made! Total payment: ${total_price:.2f}")
                except ValueError as e:
                    print(f"Error processing order: {e}")
            else:
                print("No order placed.")

        elif choice == '4':
            print("Thank you for using our store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    buy_two_get_one_free = BuyTwoGetOneFree("Buy 2, Get 1 Free!")
    thirty_percent = PercentageDiscount("30% off!", percentage=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(buy_two_get_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create the store with the product list
    best_buy = Store(product_list)

    # Start the store interface
    start(best_buy)


if __name__ == "__main__":
    main()

