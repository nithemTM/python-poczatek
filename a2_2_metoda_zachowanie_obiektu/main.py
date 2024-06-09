from a2_2_metoda_zachowanie_obiektu.shop.order import Order, generate_order
from a2_2_metoda_zachowanie_obiektu.shop.product import Product
from a2_2_metoda_zachowanie_obiektu.shop.apple import Apple
from a2_2_metoda_zachowanie_obiektu.shop.potato import Potato


def call_object():
    # Zad 1

    auto = Product(name="Honda Accord", category_name="Cars", unit_price=120000)
    circular_saw = Product(name="Bosh Circular X100", category_name="Saw", unit_price=1000)

    auto.print_product()
    circular_saw.print_product()

    list_1 = [auto, circular_saw]
    order_1 = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", products_list=list_1)
    order_1.print_order()
    generate_order()

    # Zad 2

    apple_ord = Apple(species="Golden", size=1, price=3)
    potato_ord = Potato(species="Lord", size=2, price=4)

    apple_ord.total_price_f(10)
    potato_ord.total_price_f(15)
    print(f'Cena jabłek total: {apple_ord.total_price}')
    print(f'Cena ziemniaków total: {potato_ord.total_price}')



if __name__ == "__main__":
    call_object()
