import random
from a2_3_metody_magiczne.shop.product import Product
from a2_3_metody_magiczne.shop.order_element import OrderElement


class Order:
    def __init__(self, customer_first_name, customer_last_name, order_elements=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if order_elements is None:
            order_elements = []

        self.order_elements = order_elements
        self.total_price = self.total_price_f()

    # Zad 1
    def __str__(self):
        element_print = ""
        for element in self.order_elements:
            element_print += "\n"
            element_print += str(element)

        return (f'[ Show order ]\nCustomer Data: {self.customer_first_name} {self.customer_last_name}\n'
                f'Items of Order: {element_print}\nTotal cost of order: {self.total_price}')

    # Zad 3
    def __len__(self):
        return len(self.order_elements)

    # Zad 4c
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self.order_elements) != len(other.order_elements):
            return False

        if self.customer_first_name != other.customer_first_name or self.customer_last_name != other.customer_last_name:
            return False

        for element in self.order_elements:
            if element not in other.order_elements:
                return False
        return True

    def total_price_f(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.total_price_f()

        return total_price


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
    print(random_order)
    # Zad 3
    print(f"Number of order items: {len(random_order)}")
