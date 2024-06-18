from a2_5_metody_i_pola_klasy_oraz_metody_statyczne.shop.tax_calculator import TaxCalculator


class OrderElement:
    def __init__(self, product_info, quantity_ord):
        self.product_info = product_info
        self.quantity_ord = quantity_ord
        # Zad 3
        self.tax = TaxCalculator.calculate_tax(self.total_price_f(), self.product_info.category_name)

    def __str__(self):
        return f'{self.product_info}\n\t\t x {self.quantity_ord}  Tax: {self.tax}'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product_info == other.product_info and self.quantity_ord == other.quantity_ord

    def total_price_f(self):
        return self.product_info.unit_price * self.quantity_ord


