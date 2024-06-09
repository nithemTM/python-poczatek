class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = int(unit_price)

    def print_product(self):
        print(f'Name: {self.name} - Category: {self.category_name} - Unit Price: {self.unit_price}')