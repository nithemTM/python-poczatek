# Zad 1a
import random
from a3_1_prosta_refaktoryzacja.shop.order_element import OrderElement
from a3_1_prosta_refaktoryzacja.shop.product import Product
from a3_1_prosta_refaktoryzacja.shop.order import Order

# Zad 1c
UNIT_PRICE_MIN = 1
UNIT_PRICE_MAX = 50
QUANTITY_MIN = 1
QUANTITY_MAX = 10


# Zad 1b
def generate_order(max_element=None):

    if max_element is None:
        max_element = random.randint(1, Order.MAX_ELEMENT_ORDER)
    order_elements = []
    element_sample = random.sample(range(1, max_element + 20), max_element)
    for i, prod in enumerate(element_sample):

        if i % 2 == 0:
            category = "Owoce i warzywa"
        elif i % 3 == 0:
            category = "Jedzenie"
        else:
            category = f"Some category-{prod}"
        product = Product(name=f"Product-{str(prod)}", category_name=category,
                          unit_price=random.randint(UNIT_PRICE_MIN, UNIT_PRICE_MAX))

        element = OrderElement(product_info=product, quantity_ord=random.randint(QUANTITY_MIN, QUANTITY_MAX))
        order_elements.append(element)

    return order_elements
