class Apple:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price
        self.total_price = 0

    def __repr__(self):
        return f"APPLE data: [Species - {self.species}, Size - {self.size}, Price - {self.price}, Total Price - {self.total_price}]"

    def total_price_f(self, weight):
        self.total_price = weight * self.price
