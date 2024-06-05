#from a1_2_rozne_sposoby_importowania.store.products import products
from .products import products

orders = []


def make_order(product, quantity_ord):

    if products[product]["quantity"] >= quantity_ord:
        products[product]["quantity"] -= quantity_ord
        payment = products[product]["price"] * quantity_ord
        one_order = {
            "product": product,
            "quantity_ord": quantity_ord,
            "payment": payment
        }
        orders.append(one_order)
        return one_order
    else:
        print(f'Niewystarczająca ilość art w zapasie sklepu! możesz zamówić max. {products[product]["quantity"]}')


