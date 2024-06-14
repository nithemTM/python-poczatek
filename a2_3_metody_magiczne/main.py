from a2_3_metody_magiczne.shop.order import Order, generate_order
from a2_3_metody_magiczne.shop.product import Product
from a2_3_metody_magiczne.shop.apple import Apple
from a2_3_metody_magiczne.shop.potato import Potato
from a2_3_metody_magiczne.shop.order_element import OrderElement


def call_object():

    # Zad 1
    auto = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw = Product(name="Bosh Circular X100", category_name="Saw", unit_price=1000)

    print(auto)
    print(circular_saw)

    product_1 = OrderElement(product_info=auto,quantity_ord=2)
    product_2 = OrderElement(product_info=circular_saw,quantity_ord=9)
    product_list = [product_1, product_2]
    product_list_1 = [product_1, product_1]
    order_1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", order_elements=product_list)

    print(order_1)
    # Zad 3
    print(f"Number of order items: {len(order_1)}")

    generate_order()

    # Zad 2
    apple = Apple("Special", 2, 3)
    potato = Potato("Lord",1,4)
    print(apple)
    print(potato)

    # Zad 4a
    auto2 = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw2 = Product(name="Bosh Circular X101", category_name="Saw", unit_price=1000)

    print(f"auto = {auto}")
    print(f"auto2 = {auto2}")
    print(f"circular_saw = {circular_saw}")
    print(f"circular_saw2 = {circular_saw2}")
    print(f"Czy auto == auto2? {auto == auto2}")
    print(f"Czy circular_saw == circular_saw2? {circular_saw == circular_saw2}")

    # Zad 4b
    order_2 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", order_elements=product_list)
    print(f"Czy pozycja 1 w zamówieniu order_2 == 2 pozycji? {order_2.order_elements[0] == order_2.order_elements[1]}")
    order_3 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", order_elements=product_list_1)
    print(f"Czy pozycja 1 w zamówieniu order_3 == 2 pozycji? {order_3.order_elements[0] == order_3.order_elements[1]}")

    # Zad 4c
    order_4 = Order(customer_first_name="Michał", customer_last_name="Tokarski", order_elements=product_list_1)
    print(f"Czy zamówienie order_3 == zamówieniu order_4? {order_3 == order_4}")
    print(f"Czy zamówienie order_2 == zamówieniu order_3? {order_2 == order_3}")
    print(f"Czy zamówienie order_2 == zamówieniu order_2? {order_2 == order_2}")


if __name__ == "__main__":
    call_object()
