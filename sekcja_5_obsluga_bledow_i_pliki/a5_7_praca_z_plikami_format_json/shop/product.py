from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    FOOD = "Jedzenie"
    TOOLS = "Narzędzia"
    OTHER = "Some category"


@dataclass
class Product:
    name: str
    category_name: ProductCategory
    unit_price: int
    identifier: int

    def __str__(self):
        return f'Name: {self.name} - Category: {self.category_name.value} - Unit Price: {self.unit_price}'


@dataclass
class ProductTerm(Product):
    year_production: int
    amount_years: int

    def does_expire(self, current_year):
        if (current_year - self.year_production) > self.amount_years:
            return True
        else:
            return False

