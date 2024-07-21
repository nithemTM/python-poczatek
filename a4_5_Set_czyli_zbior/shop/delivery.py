import random


# Zad 1

def products_delivery():

    product_list = ["kiełbasa", "jabłka", "chleb", "masło", "marchew", "mleko", "bułka", "kapusta", "kurczak", "chipsy"]

    return [random.choice(product_list) for _ in range(0, 5)]