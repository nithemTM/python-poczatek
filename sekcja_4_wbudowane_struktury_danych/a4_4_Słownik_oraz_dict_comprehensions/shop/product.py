class Product:

    def __init__(self, name, category_name, unit_price, identifier):
        self.name = name
        self.category_name = category_name
        self.unit_price = int(unit_price)
        # Zad 1
        self.identifier = identifier

    def __str__(self):
        return f'Id: { self.identifier} - Name: {self.name} - Category: {self.category_name} - Unit Price: {self.unit_price}'

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (
                self.name == other.name
                and self.category_name == other.category_name
                and self.unit_price == other.unit_price
        )


class ProductTerm(Product):

    def __init__(self, name, category_name, unit_price, identifier, year_production, amount_years):
        super().__init__(name, category_name, unit_price, identifier)
        self.year_production = year_production
        self.amount_years = amount_years

    def does_expire(self, current_year):
        if (current_year - self.year_production) > self.amount_years:
            return True
        else:
            return False
