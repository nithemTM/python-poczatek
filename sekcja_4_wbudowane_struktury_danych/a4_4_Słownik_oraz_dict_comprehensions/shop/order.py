from sekcja_4_wbudowane_struktury_danych.a4_4_Słownik_oraz_dict_comprehensions.shop.order_element import OrderElement


class Order:

    MAX_ELEMENT_ORDER = 10

    def __init__(self, customer_first_name, customer_last_name, discount_policy=None, order_elements=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if order_elements is None:
            order_elements = []

        if len(order_elements) > Order.MAX_ELEMENT_ORDER:
            print("Note! Some units have been cut out - To much elements of this order.")
            order_elements = order_elements[:Order.MAX_ELEMENT_ORDER]
        self.total_price_origin = 0
        self._order_elements = order_elements
        self.discount_policy = discount_policy
        self.total_price_n, self.discount = self.total_price
        # self.total_price, self.discount = self._total_price_f()

    def __str__(self):
        element_print = ""
        for element in self._order_elements:
            element_print += "\n"
            element_print += str(element)

        return (f'[ Show order ]\nCustomer Data: {self.customer_first_name} {self.customer_last_name}\n'
                f'Items of Order: {element_print}\nTotal cost of order: {self.total_price}'
                f'\nDiscount: {self.discount}\nTotal price: {self.total_price_n}'
                f'\nTotal price origin: {self.total_price_origin}')

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

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ELEMENT_ORDER:
            self._order_elements = value
        else:
            self._order_elements = value[:Order.MAX_ELEMENT_ORDER]
        # self.total_price, self.discount = self._total_price_f()

    @property
    def total_price(self):
        return self._total_price_f()

    def _total_price_f(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.total_price_f()

        if self.discount_policy:
            self.total_price_origin = total_price

            return self.discount_policy.apply_discount(total_price=total_price)
        else:
            self.total_price_origin = total_price
            return total_price, "Default"

    def add_new_art(self, product_info, quantity_ord):

        if len(self._order_elements) < Order.MAX_ELEMENT_ORDER:
            new_element = OrderElement(product_info, quantity_ord)
            self._order_elements.append(new_element)
            # self.total_price = self._total_price_f()
        else:
            print("Note! Can't create new item, to much elements of this order.")


class ExpressOrder(Order):

    DELIVERY_TAX = 5

    def __init__(self, customer_first_name, customer_last_name, discount_policy=None, order_elements=None, delivery_term="01-01-1900"):
        super().__init__(customer_first_name, customer_last_name, discount_policy, order_elements)
        self.delivery_term = delivery_term
        self.total_price_origin = 0
        #self.total_price_n = self.total_price_n + self.DELIVERY_TAX

    # Zad 1
    def _total_price_f(self):
        total_price_n, discount = super()._total_price_f()
        return total_price_n+self.DELIVERY_TAX, discount

    def __str__(self):
        element_print = ""
        for element in self._order_elements:
            element_print += "\n"
            element_print += str(element)
        return (f'[ Show order ]\nCustomer Data: {self.customer_first_name} {self.customer_last_name}\n'
                f'Items of Order: {element_print}\nTotal cost of order: {self.total_price}\nDiscount: {self.discount}'
                f'\nTotal Price Origin: {self.total_price_origin}'
                f'\nTotal Price ++(increased by {self.DELIVERY_TAX}): {self.total_price_n}'
                f'\nDelivery Term: {self.delivery_term}')

