from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.order import Order
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.store import Store
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.error_expectation import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.file_action import save_order, see_history, choose_action


def handle_customer():
    say_hello()
    select = choose_action()
    print(select)
    if select == 1:
        order = init_order()
        while want_more_products():
            add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
        print_order_summary(order)
        save_order(order)
    elif select == 2:
        orders = see_history()
        print(orders)


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    first_name = input("Imie: " )
    last_name = input("Nazwisko: " )
    order = Order(customer_first_name=first_name, customer_last_name=last_name)
    return order


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:

        print(f"Input error!"
              f"Details: {input_error}")
        return

    try:
        order.add_new_art(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):

    if product_index_str.isnumeric():
        product_index_str = int(product_index_str)
        if 0 <= product_index_str <= max_index:
            print(f"inndex{max_index}")
            print(f"inndex_{product_index_str}")
        else:
            raise NotValidInput("Out of index list!")
        return product_index_str
    else:
        raise NotValidInput("Nieprawidłowy wpis!")


def parse_quantity(quantity_str):

    if quantity_str.isnumeric():
        quantity_str = int(quantity_str)
        if quantity_str <= 0:
            raise NotValidInput("Zbyt mała wartość!")
        return quantity_str
    else:
        raise NotValidInput("Nieprawidłowy wpis!")


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")