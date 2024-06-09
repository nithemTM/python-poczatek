from a2_1_konstruktor_i_pola_obiektu.shop.order import Order, print_order, generate_order
from a2_1_konstruktor_i_pola_obiektu.shop.product import Product, print_product


def call_object():
    auto = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw = Product(name="Bosh Circular X100", category_name="Saw", unit_price=1000)
    print_product(auto)
    print_product(circular_saw)
    list_1 = [auto, circular_saw]
    order_1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", products_list=list_1)
    print_order(order_1)
    generate_order()


if __name__ == "__main__":
    call_object()
