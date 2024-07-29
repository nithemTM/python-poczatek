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

    # def __init__(self, name, category_name, unit_price, year_production, amount_years):
    #     super().__init__(name, category_name, unit_price)
    #     self.year_production = year_production
    #     self.amount_years = amount_years

    # def __eq__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return (
    #             self.name == other.name
    #             and self.category_name == other.category_name
    #             and self.unit_price == other.unit_price
    #     )