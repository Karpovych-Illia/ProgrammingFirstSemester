"""
Лаба 3 Створими міні магазин в консолі.
Повинно бути можливість переглянути каталог товарів, добавити товар в кошик,
видалити товар з кошика, купити товари з кошика.
Створити можливість увійти як адміністратор та побачити залишки.
Використати лямбда функції. Ціни повертають у форматі ххх.ххгрн.
Використовуєм усі принципи які розібрали на лекції.
"""


products = {
    "Iphone": {"price": 32000.99, "amount": 4},
    "MacBook Air": {"price": 54999.00, "amount": 3},
    "AirPods Pro": {"price": 8999.00, "amount": 8},
    "Apple Watch": {"price": 18999.00, "amount": 6},
    "iPad": {"price": 25999.00, "amount": 5},
}

cart = []
admin_password = "123"

total_price = lambda: sum(products[item]["price"] for item in cart)


def after_delete_menu():
    while True:
        choice = input(
            "Pay - 1, add product - 2, delete item - 3, "
            "view cart - 4, exit - 0: "
        )

        if choice == "1":
            if not cart:
                print("There is nothing to pay for. Cart is empty.")
                continue

            print(f"Total: {total_price():.2f} UAH")
            print("Thank u for your purchase!")
            cart.clear()
            return

        elif choice == "2":
            product_to_cart = input("Enter product name: ")

            if product_to_cart in products:
                if products[product_to_cart]["amount"] > 0:
                    cart.append(product_to_cart)
                    products[product_to_cart]["amount"] -= 1
                    print(f"{product_to_cart} added to cart.")
                else:
                    print("Product is out of stock.")
            else:
                print("Product not found.")

        elif choice == "3":
            if not cart:
                print("There is nothing to delete. Cart is empty.")
                continue

            print("Items in your cart:")

            for item in cart:
                print(f" - {item}")

            item_to_delete = input(
                "Enter the name of the item you want to delete: "
            )

            if item_to_delete in cart:
                cart.remove(item_to_delete)
                products[item_to_delete]["amount"] += 1
                print(f"{item_to_delete} removed from cart.")
            else:
                print("Item not found in cart.")

        elif choice == "4":
            if not cart:
                print("Your cart is empty.")
            else:
                print("Items in your cart:")

                for item in cart:
                    print(
                        f" - {item}: "
                        f"{products[item]['price']:.2f} UAH"
                    )

                print(f"Total: {total_price():.2f} UAH")

        elif choice == "0":
            for item in cart:
                products[item]["amount"] += 1

            cart.clear()
            print("Goodbye! Unpaid items were returned to stock.")
            return

        else:
            print("Invalid choice.")


def logged_as_user():
    while True:
        print("========CATALOG========")

        for product, info in products.items():
            print(f"{product}: {info['price']:.2f} UAH")

        print("Wanna add something to your cart?")

        product_to_cart = input(
            "Enter product name or type 'exit' if u wanna leave: "
        )

        if product_to_cart in products:
            if products[product_to_cart]["amount"] > 0:
                cart.append(product_to_cart)
                products[product_to_cart]["amount"] -= 1
                print(f"{product_to_cart} added to cart.")
            else:
                print("Product is out of stock.")

        elif product_to_cart == "exit":
            if cart:
                after_delete_menu()
            else:
                print("Your cart is empty. Goodbye!")

            return

        else:
            print("Product not found.")


def main():
    print("Welcome to the store!")

    account = int(
        input("If u wanna login as admin - type 1, as guest - 2: ")
    )

    if account == 1:
        password = input("Enter admin password: ")

        if password == admin_password:
            print("Login successful. You are logged in as admin.")
            print("========PRODUCTS LEFT========")

            for product, info in products.items():
                print(f"{product}: {info['amount']} units left")

        else:
            print("Incorrect password.")

    elif account == 2:
        logged_as_user()

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
