from sekcja_2_prog_obiektowe_1.a2_6_funkcja_jako_obiekt.shop.order import Order
from sekcja_2_prog_obiektowe_1.a2_6_funkcja_jako_obiekt.shop.discount_policy import default_policy, discount_all_item, discount_holiday


# Zad 1
def sort_order_elements(order):
    return order.total_price


def call_object():
    # Zad 2
    order_elements = Order.generate_order(5)
    random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                         order_elements=order_elements, discount_policy=discount_holiday)
    rando_order1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                         order_elements=order_elements, discount_policy=discount_all_item)
    rando_order2 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
                         order_elements=order_elements)
    # Zad 1
    random_orders = [random_order, rando_order1, rando_order2]
    random_orders.sort(key=sort_order_elements)
    print("Zamówienia po sortowaniu:")
    for i, order in enumerate(random_orders):
        print(f"\nZAMÓWIENIE: {i+1}\n\n{order}")

    # auto = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    # circular_saw = Product(name="Bosh Circular X100", category_name="Saw", unit_price=1000)
    #
    # print(auto)
    # print(circular_saw)
    #
    # product_1 = OrderElement(product_info=auto,quantity_ord=2)
    # product_2 = OrderElement(product_info=circular_saw,quantity_ord=9)
    # product_list = [product_1, product_2]
    # product_list_1 = [product_1, product_1]
    # order_1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", order_elements=product_list)
    # print(order_1)
    # print(f"Number of order items: {len(order_1)}")

    # apple = Apple("Special", 2, 3)
    # potato = Potato("Lord",1,4)
    # print(apple)
    # print(potato)

    # auto2 = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    # circular_saw2 = Product(name="Bosh Circular X101", category_name="Saw", unit_price=1000)

    # print(f"auto = {auto}")
    # print(f"auto2 = {auto2}")
    # print(f"circular_saw = {circular_saw}")
    # print(f"circular_saw2 = {circular_saw2}")
    # print(f"Czy auto == auto2? {auto == auto2}")
    # print(f"Czy circular_saw == circular_saw2? {circular_saw == circular_saw2}")

    # print(f'Stare zamówienie: {order_1}')
    # print("Dodanie nowego art do zamówienia")
    # order_1.add_new_art(product_info=circular_saw2, quantity_ord=5)
    # print(f'Nowe zamówienie: {order_1}')


if __name__ == "__main__":
    call_object()
