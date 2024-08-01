import random

from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.error_expectation import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.product import Product, ProductCategory


class AvailableProduct:

    def __init__(self, quantity, name, category, unit_price=None, identifier=None):
        if unit_price is None:
            unit_price = random.randint(1, 100)
        if identifier is None:
            identifier = random.randint(1, 100)

        self.quantity = quantity
        self.product = Product(name=name, category_name=category, unit_price=unit_price, identifier=identifier)


class Store:
    AVAILABLE_PRODUCTS = [
        AvailableProduct(quantity=2, name="Młotek", category=ProductCategory.TOOLS),
        AvailableProduct(quantity=5, name="Chleb", category=ProductCategory.FOOD),
        AvailableProduct(quantity=1, name="Kosiarka", category=ProductCategory.TOOLS),
        AvailableProduct(quantity=1, name="Rower", category=ProductCategory.OTHER),
    ]

    @staticmethod
    def reserve_product(product, quantity):

        for available_product in Store.AVAILABLE_PRODUCTS:
            if available_product.product == product:
                print(f"dostepnosc:{available_product.quantity}")
                if available_product.quantity >= quantity:
                    available_product.quantity = available_product.quantity - quantity
                    return
                else:
                    raise TemporaryOutOfStock(product.name, available_product.quantity)
        raise ProductNotAvailable(product.name)

