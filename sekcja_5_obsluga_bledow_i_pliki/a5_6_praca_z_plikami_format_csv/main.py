from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.user_interface import handle_customer
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.store import Store
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.file_action import reader_store, writer_store, dict_reader_store, dict_writer_store


def call_object():

    # Zad 1
    Store.AVAILABLE_PRODUCTS = reader_store()
    handle_customer()

    # Zad 2
    writer_store(Store.AVAILABLE_PRODUCTS)

    # Zad 3
    Store.AVAILABLE_PRODUCTS = dict_reader_store()
    handle_customer()
    dict_writer_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    call_object()