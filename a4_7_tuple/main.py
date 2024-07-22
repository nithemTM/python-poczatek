from a4_7_tuple.shop.product import Product


def test_product():

    # Zad 1
    parameters = [
        ("chleb", "pieczywo", 5, "chleb", "pieczywo", 5, True),
        ("masło", "mleczne", 4, "masło", "mleczne", 5, False),
        ("maslo", "mleczne", 4, "masło", "mleczne", 4, False),
        ("masło", "mlecznee", 4, "masło", "mleczne", 4, False)
    ]

    for parameter in parameters:
        name, category_name, unit_price, name1, category_name1, unit_price1, result = parameter
        product = Product(name, category_name, unit_price)
        product1 = Product(name1, category_name1, unit_price1)
        if (product == product1) == result:
            print("OK")
        else:
            print(f"Blad! Dla {parameter} wynik porownania to {product == product1} zamiast {result}")


if __name__ == "__main__":
    test_product()
