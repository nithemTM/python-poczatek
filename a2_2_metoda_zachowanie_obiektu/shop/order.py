import random
from a2_2_metoda_zachowanie_obiektu.shop.product import Product


class Order:
    def __init__(self, customer_first_name, customer_last_name, products_list=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if products_list is None:
            products_list = []

        self.products_list = products_list

        total_price = 0
        for product in products_list:
            total_price += product.unit_price

        self.total_price = total_price

    def print_order(self):
        print('[ Show order ]')
        print(f'Customer Data: {self.customer_first_name} {self.customer_last_name}')
        print(f'Items of Order:')
        for product in self.products_list:
            product.print_product()
        print(f'Total cost of order: {self.total_price}')


def generate_order():

    a = random.randint(7, 20)
    product_list = []
    b = random.sample(range(1, a + 1), 6)
    for prod in b:
        product = Product(name=f"Product-{str(prod)}", category_name=f"Some category-{prod}",
                          unit_price=random.randint(1, 50))
        product_list.append(product)

    random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                         products_list=product_list)
    random_order.print_order()