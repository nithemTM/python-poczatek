import random
from sekcja_5_obsluga_bledow_i_pliki.a5_5_praca_z_plikami_konstrukcja_with.shop.order_element import OrderElement
from sekcja_5_obsluga_bledow_i_pliki.a5_5_praca_z_plikami_konstrukcja_with.shop.product import Product, ProductCategory
from sekcja_5_obsluga_bledow_i_pliki.a5_5_praca_z_plikami_konstrukcja_with.shop.order import Order


UNIT_PRICE_MIN = 1
UNIT_PRICE_MAX = 50
QUANTITY_MIN = 1
QUANTITY_MAX = 10


def generate_order(max_element=None):

    if max_element is None:
        max_element = random.randint(1, Order.MAX_ELEMENT_ORDER)
    order_elements = []
    element_sample = random.sample(range(1, max_element + 20), max_element)
    for i, prod in enumerate(element_sample):
        if i % 2 == 0:
            category = ProductCategory.TOOLS
        elif i % 3 == 0:
            category = ProductCategory.FOOD
        else:
            category = ProductCategory.OTHER
        product = Product(name=f"Product-{str(prod)}", category_name=category,
                          unit_price=random.randint(UNIT_PRICE_MIN, UNIT_PRICE_MAX), identifier=1)

        element = OrderElement(product_info=product, quantity_ord=random.randint(QUANTITY_MIN, QUANTITY_MAX))
        order_elements.append(element)

    return order_elements
