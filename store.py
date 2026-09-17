import products


class Store:

    def __init__(self, product_list):
        self.products = product_list[:]


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)


    def get_all_products(self):
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        total = 0

        for product, quantity in shopping_list:
            total += product.buy(quantity)

        return total
