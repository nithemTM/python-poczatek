import random
from sekcja_2_prog_obiektowe_1.a2_5_metody_i_pola_klasy_oraz_metody_statyczne.shop.product import Product
from sekcja_2_prog_obiektowe_1.a2_5_metody_i_pola_klasy_oraz_metody_statyczne.shop.order_element import OrderElement


class Order:
    # Zad 1
    MAX_ELEMENT_ORDER = 2

    def __init__(self, customer_first_name, customer_last_name, order_elements=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if order_elements is None:
            order_elements = []
        # Zad 1
        if len(order_elements) > Order.MAX_ELEMENT_ORDER:
            print("Note! Some units have been cut out - To much elements of this order.")
            order_elements = order_elements[:Order.MAX_ELEMENT_ORDER]
        self._order_elements = order_elements
        self.total_price = self._total_price_f()

    def __str__(self):
        element_print = ""
        for element in self._order_elements:
            element_print += "\n"
            element_print += str(element)

        return (f'[ Show order ]\nCustomer Data: {self.customer_first_name} {self.customer_last_name}\n'
                f'Items of Order: {element_print}\nTotal cost of order: {self.total_price}')

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other.order_elements):
            return False

        if self.customer_first_name != other.customer_first_name or self.customer_last_name != other.customer_last_name:
            return False

        for element in self._order_elements:
            if element not in other.order_elements:
                return False
        return True

    # Zad 1
    def _total_price_f(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.total_price_f()

        return total_price

    # Zad 1
    def add_new_art(self, product_info, quantity_ord):
        # Zad 1
        if len(self._order_elements) < Order.MAX_ELEMENT_ORDER:
            new_element = OrderElement(product_info, quantity_ord)
            self._order_elements.append(new_element)
            self.total_price = self._total_price_f()
        else:
            print("Note! Can't create new item, to much elements of this order.")

    # Zad 2
    @classmethod
    def generate_order(cls, max_element):  # Zad 1

        a = random.randint(max_element+1, max_element+13)
        order_elements = []
        b = random.sample(range(1, a + 1), max_element)
        for i, prod in enumerate(b):
            # Zad 3
            if i % 2 == 0:
                category = "Owoce i warzywa"
            elif i % 3 == 0:
                category = "Jedzenie"
            else:
                category = f"Some category-{prod}"
            product = Product(name=f"Product-{str(prod)}", category_name=category,
                              unit_price=random.randint(1, 50))

            element = OrderElement(product_info=product, quantity_ord=random.randint(1, 10))
            order_elements.append(element)

        random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                             order_elements=order_elements)
        print(random_order)
        print(f"Number of order items: {len(random_order)}")
