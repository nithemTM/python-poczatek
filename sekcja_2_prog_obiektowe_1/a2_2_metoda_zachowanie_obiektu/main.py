from sekcja_2_prog_obiektowe_1.a2_2_metoda_zachowanie_obiektu.shop.order import Order, generate_order
from sekcja_2_prog_obiektowe_1.a2_2_metoda_zachowanie_obiektu.shop.product import Product
from sekcja_2_prog_obiektowe_1.a2_2_metoda_zachowanie_obiektu.shop.order_element import OrderElement


def call_object():
    # Zad 3

    auto = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw = Product(name="Bosh Circular X100", category_name="Saw", unit_price=1000)

    auto.print_product()
    circular_saw.print_product()

    product_1 = OrderElement(product_info=auto,quantity_ord=2)
    product_2 = OrderElement(product_info=circular_saw,quantity_ord=9)
    product_list = [product_1, product_2]
    order_1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", order_elements=product_list)
    order_1.print_order()
    generate_order()





if __name__ == "__main__":
    call_object()
