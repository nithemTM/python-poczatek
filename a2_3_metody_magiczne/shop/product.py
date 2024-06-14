class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = int(unit_price)

    # Zad 1
    def __str__(self):
        return f'Name: {self.name} - Category: {self.category_name} - Unit Price: {self.unit_price}'

    # Zad 4a
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (
                self.name == other.name
                and self.category_name == other.category_name
                and self.unit_price == other.unit_price
        )
