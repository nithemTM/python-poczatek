import csv
import os
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.store import AvailableProduct
from sekcja_5_obsluga_bledow_i_pliki.a5_6_praca_z_plikami_format_csv.shop.product import ProductCategory


# Zad 1
def reader_store():
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "werhouse.csv")
    store_available = []
    with open(path_file, newline="") as available_store:
        csv_reader = csv.reader(available_store)
        print(csv_reader)
        next(csv_reader)
        for row_index, row in enumerate(csv_reader):
            print(row[0])
            product = AvailableProduct(quantity=int(row[4]), name=row[0], category=ProductCategory[row[1]], unit_price=int(row[2]), identifier=int(row[3]))
            store_available.append(product)

    return store_available


# Zad 2
def writer_store(currenty_store):
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "werhouse.csv")
    with open(path_file, mode="w", newline="") as available_store_write:
        csv_writer = csv.writer(available_store_write)
        csv_writer.writerow(["name","category_name","unit_price","identifier","quantity"])
        for product_next in currenty_store:
            csv_writer.writerow(
                [
                    product_next.product.name,
                    product_next.product.category_name.name,
                    product_next.product.unit_price,
                    product_next.product.identifier,
                    product_next.quantity
                ]
            )


# Zad 3
def dict_reader_store():
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "werhouse.csv")
    store_available = []
    with open(path_file, newline="") as available_store:
        csv_reader = csv.DictReader(available_store)
        for row_index, row in enumerate(csv_reader):
            print(row["name"])
            product = AvailableProduct(quantity=int(row["quantity"]), name=row["name"], category=ProductCategory[row["category_name"]], unit_price=int(row["unit_price"]), identifier=int(row["identifier"]))
            store_available.append(product)

    return store_available


def dict_writer_store(currenty_store):
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "werhouse.csv")
    with open(path_file, mode="w", newline="") as available_store_write:
        header = ["name","category_name","unit_price","identifier","quantity"]

        csv_writer = csv.DictWriter(available_store_write, fieldnames=header)
        csv_writer.writeheader()
        for product_next in currenty_store:
            csv_writer.writerow(
                {
                    "name": product_next.product.name,
                    "category_name": product_next.product.category_name.name,
                    "unit_price": product_next.product.unit_price,
                    "identifier": product_next.product.identifier,
                    "quantity": product_next.quantity,
                }
            )


def choose_action():
    try:
        a = int(input("1 - New Order\n"
                  "2 - History Orders\n"
                  ">> "))
        if a == 1:
            return 1
        elif a == 2:
            return 2
    except ValueError:
        print("Wrong input!")


def see_history():
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "orders.txt")
    try:
        with open(path_file, mode="r") as orders_txt:
            return orders_txt.read()
    except IOError:
        print("Bład przy otwieraniu pliku!")
    finally:
        print("Zamykamy plik")
        orders_txt.close()


def save_order(order):
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "orders.txt")
    try:
        with open(path_file, mode="a") as orders_txt:
            orders_txt.write(str(order))
            orders_txt.write("\n\n\n2")
    except IOError:
        print("Bład przy otwieraniu pliku!")
    finally:
        print("Zamykamy plik")
        orders_txt.close()


