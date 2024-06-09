import random
from a2_2_metoda_zachowanie_obiektu.shop.product import Product
from a2_2_metoda_zachowanie_obiektu.shop.order_element import OrderElement


class Order:
    def __init__(self, customer_first_name, customer_last_name, order_elements=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if order_elements is None:
            order_elements = []

        self.order_elements = order_elements
        self.total_price = self.total_price_f()

    def total_price_f(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.total_price_f()

        return total_price

    def print_order(self):
        print('[ Show order ]')
        print(f'Customer Data: {self.customer_first_name} {self.customer_last_name}')
        print(f'Items of Order:')
        for element in self.order_elements:
            element.print_info()
        print(f'Total cost of order: {self.total_price}')


def generate_order():

    a = random.randint(7, 20)
    order_elements = []
    b = random.sample(range(1, a + 1), 6)
    for prod in b:
        product = Product(name=f"Product-{str(prod)}", category_name=f"Some category-{prod}",
                          unit_price=random.randint(1, 50))

        element = OrderElement(product_info=product, quantity_ord=random.randint(1, 10))
        order_elements.append(element)

    random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                         order_elements=order_elements)
    random_order.print_order()