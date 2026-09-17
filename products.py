class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Product name cannot be empty")

        if price < 0:
            raise Exception("Product price cannot be negative")

        if quantity < 0:
            raise Exception("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is sold out")

        if quantity > self.quantity:
            raise Exception("Not enough items in stock")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price
