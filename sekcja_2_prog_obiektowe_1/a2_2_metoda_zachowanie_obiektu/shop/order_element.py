class OrderElement:
    def __init__(self, product_info, quantity_ord):
        self.product_info = product_info
        self.quantity_ord = quantity_ord

    def total_price_f(self):
        return self.product_info.unit_price * self.quantity_ord

    def print_info(self):
        self.product_info.print_product()
        print(f'\t\t x {self.quantity_ord}')

