import random


class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = int(unit_price)


class Order:
    def __init__(self, customer_first_name, customer_last_name, products_list=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

        if products_list is None:
            products_list = []

        self.products_list = products_list

        total_price = 0
        for product in products_list:
            total_price += product.unit_price

        self.total_price = total_price


class Apple:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price


def print_product(product):
    print(f'Name: {product.name} - Category: {product.category_name} - Unit Price: {product.unit_price}')


def print_order(order):
    print('[ Show order ]')
    print(f'Customer Data: {order.customer_first_name} {order.customer_last_name}')
    print(f'Items of Order:')
    for product in order.products_list:
        print_product(product)
    print(f'Total cost of order: {order.total_price}')


def generate_order():

    a = random.randint(7, 20)
    product_list = []
    b = random.sample(range(1, a + 1), 6)
    for prod in b:
        product = Product(name=f"Product-{str(prod)}", category_name=f"Some category-{prod}", unit_price=random.randint(1,50))
        product_list.append(product)

    random_order = Order(customer_first_name="Mateusz", customer_last_name="Tokarski", products_list=product_list)
    print_order(random_order)


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

# potato = Potato()
# sweet_potato = Potato()
#
# print(f"red_apple is type: {type(red_apple)}")
# print(f"green_apple is type: {type(green_apple)}")
#
# print(f"potato is type: {type(potato)}")
# print(f"sweet_potato is type: {type(sweet_potato)}")
#
# order = [Order(),Order(),Order(),Order(),Order()]
#
# dict_product = {
# "Apple":Product(),
# "Potato":Product(),
# "Pasta":Product(),
# "Tomato":Product(),
# }
# print(dict)