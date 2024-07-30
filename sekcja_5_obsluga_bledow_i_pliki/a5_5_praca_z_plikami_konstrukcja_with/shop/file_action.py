import os


# Zad 2
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

# Zad 1

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


