import random
from sekcja_2_prog_obiektowe_1.a2_1_konstruktor_i_pola_obiektu.shop.product import Product, print_product


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


def print_order(order):
    print('[ Show order ]')
    print(f'Customer Data: {order.customer_first_name} {order.customer_last_name}')
    print(f'Items of Order:')
    for product in order.products_list:
        print_product(product)
    print(f'Total cost of order: {order.total_price}')


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
    print_order(random_order)