from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.product import Product
from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.tax_calculator import TaxCalculator
from dataclasses import dataclass, field


@dataclass
class OrderElement:
    product_info: Product
    quantity_ord: int
    tax: float = field(init=False)

    def __post_init__(self):
        self.tax = TaxCalculator.calculate_tax(self.total_price_f(), self.product_info.category_name)

    def __str__(self):
        return f'{self.product_info}\n\t\t x {self.quantity_ord}\n\t\t [Total price: {self.total_price_f()} - Tax: {self.tax}]'

    def total_price_f(self):
        return self.product_info.unit_price * self.quantity_ord
