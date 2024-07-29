from dataclasses import dataclass


@dataclass
class Apple:
    species: str = "Gold"
    size: int = 2
    price: int = 0
    total_price: int = 0

    def total_price_f(self, weight):
        self.total_price = weight * self.price
