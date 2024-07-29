from dataclasses import dataclass


@dataclass
class Potato:
    species: str = "Lord"
    size: int = 1
    price: int = 0
    total_price: int = 0

    def total_price_f(self, weight):
        self.total_price = weight * self.price
