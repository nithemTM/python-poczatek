from a4_5_Set_czyli_zbior.shop.delivery import products_delivery


def call_object():

    # Zad 1
    products_necessary = ["kiełbasa", "jabłka", "chleb", "masło", "marchew", "mleko", "bułka", "kapusta", "kurczak", "chipsy"]
    store_product = []

    while not set(products_necessary).issubset(store_product):
        print(f"Nasz stock produktów przed nową dostawą: {store_product}")
        order_delivery = products_delivery()
        #print(order_delivery)
        order_delivery = set(order_delivery)
        order_delivery = list(order_delivery)
        store_product = store_product + list(order_delivery)

        #print(order_delivery)
        store_product = store_product + list(order_delivery)
        different_product = set(products_necessary).difference(store_product)
        print(f"Nasz stock produktów po dostawie: {store_product}")
        print(f"Brakujące produkty: {different_product}")


if __name__ == "__main__":
    call_object()

