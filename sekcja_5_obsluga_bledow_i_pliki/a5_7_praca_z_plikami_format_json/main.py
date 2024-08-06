from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.user_interface import handle_customer
from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.store import Store
from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.file_action import reader_store, writer_store, dict_reader_store, dict_writer_store


def call_object():

    Store.AVAILABLE_PRODUCTS = dict_reader_store()
    handle_customer()
    dict_writer_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    call_object()