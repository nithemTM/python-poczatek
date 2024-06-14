from a2_4_enkapsulacja_w_pythonie.shop.order import Order, generate_order
from a2_4_enkapsulacja_w_pythonie.shop.product import Product
from a2_4_enkapsulacja_w_pythonie.shop.apple import Apple
from a2_4_enkapsulacja_w_pythonie.shop.potato import Potato
from a2_4_enkapsulacja_w_pythonie.shop.order_element import OrderElement


def call_object():

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
    print(f"Number of order items: {len(order_1)}")

    generate_order()

    apple = Apple("Special", 2, 3)
    potato = Potato("Lord",1,4)
    print(apple)
    print(potato)

    auto2 = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw2 = Product(name="Bosh Circular X101", category_name="Saw", unit_price=1000)

    print(f"auto = {auto}")
    print(f"auto2 = {auto2}")
    print(f"circular_saw = {circular_saw}")
    print(f"circular_saw2 = {circular_saw2}")
    print(f"Czy auto == auto2? {auto == auto2}")
    print(f"Czy circular_saw == circular_saw2? {circular_saw == circular_saw2}")

    # Zad 1
    print(f'Stare zamówienie: {order_1}')
    print("Dodanie nowego art do zamówienia")
    order_1.add_new_art(product_info=circular_saw2, quantity_ord=5)
    print(f'Nowe zamówienie: {order_1}')



if __name__ == "__main__":
    call_object()
