import csv
import os
import json
from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.store import AvailableProduct
from sekcja_5_obsluga_bledow_i_pliki.a5_7_praca_z_plikami_format_json.shop.product import ProductCategory


# ZAD 1
def save_json(order, org_orders_data):
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "orders_j.json")
    order_data = {
        "orders": org_orders_data
    }
    new_order = {
        "customer_first_name": order.customer_first_name,
        "customer_last_name": order.customer_last_name,
        "order_elements": [
            {
                "product_name": order_element.product_info.name,
                "category_name": order_element.product_info.category_name.value,
                "unit_price": order_element.product_info.unit_price,
                "quantity": order_element.quantity_ord,
                "tax": order_element.tax,
                "payment": order_element.product_info.unit_price * order_element.quantity_ord
            } for order_element in order.order_elements],
        "total_price": order.total_price_origin
    }

    order_data["orders"].append(new_order)

    try:
        with open(path_file, mode="w") as orders_json:
            json.dump(order_data, orders_json, indent=4)
    except IOError:
        print("Bład przy otwieraniu pliku!")
    finally:
        print("Zamykamy plik2")
        orders_json.close()


def load_json():
    c_dir = os.path.dirname(__file__)
    path_file = os.path.join(c_dir, "..", "data", "orders_j.json")
    try:
        with open(path_file, mode="r") as orders_json:
            content = orders_json.read().strip()
            if not content:
                print("Pusty plik")
                return []
            orders_json.seek(0)
            orders_data = json.load(orders_json).get("orders", [])
        return orders_data
    except IOError:
        print("Bład przy otwieraniu pliku!")
    finally:
        print("Zamykamy plik1")
        orders_json.close()


# ZAD 2
def see_history_json(first_name, last_name, data_file):

    for order in data_file:
        if order["customer_first_name"] == first_name and order["customer_last_name"] == last_name:
            print(order)


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



