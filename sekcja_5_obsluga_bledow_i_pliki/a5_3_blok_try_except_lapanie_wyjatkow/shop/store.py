import random

from sekcja_5_obsluga_bledow_i_pliki.a5_3_blok_try_except_lapanie_wyjatkow.shop.error_expectation import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from sekcja_5_obsluga_bledow_i_pliki.a5_3_blok_try_except_lapanie_wyjatkow.shop.product import Product, ProductCategory


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

        # Zad 3
        for available_product in Store.AVAILABLE_PRODUCTS:
            if available_product.product == product:
                print(available_product.quantity)
                if available_product.quantity >= quantity:
                    available_product.quantity = available_product.quantity - quantity
                else:
                    raise TemporaryOutOfStock(product.name, available_product.quantity)
            raise ProductNotAvailable(product.name)

        # TODO: Przeszukaj listę dostępnych produktów.
        #  Jeżeli produkt, który zamawiamy jest na liście w odpowiedniej ilości zmniejsz jego ilość i zakończ funkcję
        #  Jeżeli produktu nie ma na liście albo jest go za mało rzuć odpowiedni wyjątek