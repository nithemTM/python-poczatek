class Apple:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price
        self.total_price = 0

    def total_price_f(self, weight):
        self.total_price = weight * self.price
