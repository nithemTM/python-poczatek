from sekcja_5_obsluga_bledow_i_pliki.a5_2_tworzenie_wlasnych_wyjatkow.shop.data_generator import generate_order
from sekcja_5_obsluga_bledow_i_pliki.a5_2_tworzenie_wlasnych_wyjatkow.shop.order import Order
from sekcja_5_obsluga_bledow_i_pliki.a5_2_tworzenie_wlasnych_wyjatkow.shop.discount_policy import DiscountPolicy
from sekcja_5_obsluga_bledow_i_pliki.a5_2_tworzenie_wlasnych_wyjatkow.shop.product import Product, ProductCategory


def call_object():
    # Zad 1 - Zwiększaj ilość w argumencie generate_order jeżeli chcesz sprawdzić kolejne wersje wyrzucanych wyjątków
    policy = DiscountPolicy()

    order_random = generate_order(10)
    order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", discount_policy=policy, order_elements=order_random)
    # Zad 1 - Zwiększaj ilość w argumencie generate_order jeżeli chcesz sprawdzić kolejne wersje wyrzucanych wyjątków
    order.order_elements = generate_order(10)
    print(order)

    # Zad 1 - Zwiększaj ilość w argumencie generate_order jeżeli chcesz sprawdzić kolejne wersje wyrzucanych wyjątków
    product = Product("ProduktNew", ProductCategory.OTHER, 3)
    order.add_new_art(product, 5)

    print(order)




if __name__ == "__main__":
    call_object()

    # frozen_pizza = ProductTerm(name="Pizza margherita", category_name="Italian Food", unit_price=20, year_production=2020, amount_years=4)
    #
    # print(frozen_pizza.does_expire(2024))
    # print(frozen_pizza.does_expire(2026))
    # def sort_order_elements(order):
    #     return order.total_price
    #
    #
    # def call_object():
    #
    #     order_elements = generate_order(7)
    #     random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
    #                          order_elements=order_elements, discount_policy=discount_holiday)
    #
    #     print("[ZAMÓWIENIE random_order]\n")
    #
    #     for i, element in enumerate(random_order.order_elements):
    #         print(f"\nelment: {i+1}\n{element}")
    #
    #     print(f"\nZAMÓWIENIE:\n\n{random_order}")
    #
    #
    #     new_elements_order = generate_order(4)
    #     random_order.order_elements = new_elements_order
    #
    #     print(f"\nZAMÓWIENIE_NEW:\n\n{random_order}")
    #
    #     new_elements_too_much = generate_order(15)
    #     random_order.order_elements = new_elements_too_much
    #
    #     print(f"\nZAMÓWIENIE_TOO_MUCH:\n\n{random_order}")

    # rando_order1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
    #                      order_elements=order_elements, discount_policy=discount_all_item)
    # rando_order2 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski",
    #                      order_elements=order_elements)
    # random_orders = [random_order, rando_order1, rando_order2]
    # random_orders.sort(key=sort_order_elements)
    # print("Zamówienia po sortowaniu:")
    # for i, order in enumerate(random_orders):
    #     print(f"\nZAMÓWIENIE: {i+1}\n\n{order}")

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
