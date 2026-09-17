import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def show_menu():
    print(
            "1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit"
        )


def list_products(store):
    for product in store.get_all_products():
        product.show()


def show_total_quantity(store):
    print(f"Total amount of products: {store.get_total_quantity()}")


def make_order(store):
    shopping_list = []
    available_products = store.get_all_products()

    while True:
        print("\nAvailable products:")

        for index, product in enumerate(available_products):
            print(f"{index + 1}. ", end="")
            product.show()

        product_choice = int(input("Please enter the product number: "))

        if product_choice < 1 or product_choice > len(available_products):
            print("Invalid product number.")
            continue

        product = available_products[product_choice - 1]

        quantity = int(input("Please enter the quantity: "))

        shopping_list.append((product, quantity))

        print(f"{quantity} {product.name} added to the shopping list.")

        another = input("Would you like to add another product? (y/n): ")

        if another.lower() != "y":
            break

    if shopping_list:
        total = store.order(shopping_list)
        print(f"Total price: ${total}")


def start(store):
    while True:
        show_menu()

        choice = input("Please choose an option: ")

        if choice == "1":
            list_products(store)

        elif choice == "2":
            show_total_quantity(store)

        elif choice == "3":
            make_order(store)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-4.")

start(best_buy)