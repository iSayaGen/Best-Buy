import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def get_integer(message):
    """Ask the user for an integer and keep retrying until valid."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_choice(message, minimum, maximum):
    """Ask for an integer within a specified range."""
    while True:
        choice = get_integer(message)

        if minimum <= choice <= maximum:
            return choice

        print(
            f"Please enter a number between "
            f"{minimum} and {maximum}."
        )


def get_positive_integer(message):
    """Ask the user for a positive integer."""
    while True:
        value = get_integer(message)

        if value > 0:
            return value

        print("Please enter a positive number.")


def get_yes_no(message):
    """Ask the user for a yes/no answer."""
    while True:
        answer = input(message).strip().lower()

        if answer in ("y", "n"):
            return answer

        print("Please enter y or n.")


def show_menu():
    """Display the store's main menu."""
    print(
            "1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit"
        )


def list_products(store):
    """Display all active products in the store."""
    available_products = store.get_all_products()

    if not available_products:
        print("I am sorry to say, there are no products available.\n"
              "The store is sold out.")
        return

    for index, product in enumerate(available_products, start=1):
        print(f"{index}. ", end="")
        product.show()


def show_total_quantity(store):
    """Display the total quantity of products in the store."""
    print(
        f"Total amount of products: {store.get_total_quantity()}")


def make_order(store):
    """Collect products and quantities and process an order."""
    shopping_list = []

    while True:
        available_products = store.get_all_products()

        if not available_products:
            print("There are no products available to order.")
            return

        print("\nAvailable products:")

        for index, product in enumerate(available_products, start=1):
            print(f"{index}. ", end="")
            product.show()

        product_choice = get_choice(
            "Please enter the product number: ",
            1,
            len(available_products)
        )

        product = available_products[product_choice - 1]

        quantity = get_choice(
            "Please enter the quantity: ",
            1,
            product.get_quantity()
        )

        shopping_list.append((product, quantity))

        print(
            f"{quantity} {product.name} "
            f"added to the shopping list."
        )

        another = get_yes_no(
            "Would you like to add another product? (y/n): "
        )

        if another == "n":
            break

    try:
        total = store.order(shopping_list)
        print(f"Total price: ${total}")
    except ValueError as error:
        print(f"Order could not be completed: {error}")


def start(store):
    """Run the store's main menu."""
    actions = {
        1: lambda: list_products(store),
        2: lambda: show_total_quantity(store),
        3: lambda: make_order(store),
    }

    while True:
        show_menu()

        choice = get_choice(
            "Please choose an option: ",
            1,
            4
        )

        if choice == 4:
            print("Goodbye!")
            break

        actions[choice]()


start(best_buy)